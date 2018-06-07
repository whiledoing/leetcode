#/usr/bin/env python
#encoding: utf-8

from abc import ABCMeta, abstractmethod
from contextlib import contextmanager
from functools import total_ordering

import collections
from threading import Lock

from itertools import chain, dropwhile, count, cycle
import random


def geometric(p):
    return (next(dropwhile(lambda _: random.randint(1, int(1. / p)) == 1, count())) for _ in cycle([1]))


@total_ordering
class NIL(object):
    """Sentinel object that always compares greater than another object"""
    __slots__ = ()

    def __lt__(self, other):
        return False

    def __eq__(self, other):
        return False

    def __str__(self):
        return 'NIL'

    def __nonzero__(self):
        return False


class _Skipnode(object):
    __slots__ = ('data', 'nxt', 'key', 'prev', 'height')

    def __init__(self, key, data, nxt, prev):
        self.key = key
        self.data = data
        self.nxt = nxt
        self.prev = prev

        for level in range(len(prev)):
            prev[level].nxt[level] = self.nxt[level].prev[level] = self


class LockableArray(list):
    def __init__(self, seq=()):
        super(LockableArray, self).__init__(seq)
        self._lock = Lock()

    @contextmanager
    def lock(self):
        try:
            yield self._lock.acquire()
        finally:
            self._lock.release()


class SkiplistAbstractBase:
    __metaclass__ = ABCMeta
    """Class for randomized indexed skip list. The default
    distribution of node heights is geometric."""

    distribution = geometric(0.5)

    @property
    @abstractmethod
    def head(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def tail(self):
        raise NotImplementedError

    def _height(self):
        return len(self.head.nxt)

    def _level(self, start=None, level=0):
        node = start or self.head.nxt[level]
        while node is not self.tail:
            yield node
            node = node.nxt[level]

    def _scan(self, key):
        return_value = None
        height = len(self.head.nxt)
        prevs = LockableArray([self.head] * height)
        node = self.head.nxt[-1]
        for level in reversed(range(height)):
            node = next(
                dropwhile(
                    lambda node_: node_.nxt[level].key <= key,
                    chain([self.head], self._level(node, level))
                )
            )
            if node.key == key:
                return_value = node
            else:
                prevs[level] = node

        return return_value, prevs

    def _insert(self, key, data):
        """Inserts data into appropriate position."""

        node, update = self._scan(key)

        if node:
            node.data = data
            return

        node_height = next(self.distribution) + 1  # because height should be positive non-zero
        # if node's height is greater than number of levels
        # then add new levels, if not do nothing
        height = len(self.head.nxt)

        update.extend([self.head for _ in range(height, node_height)])

        self.head.nxt.extend([self.tail for _ in range(height, node_height)])

        self.tail.prev.extend([self.head for _ in range(height, node_height)])

        _Skipnode(key, data, [update[l].nxt[l] for l in range(node_height)], [update[l] for l in range(node_height)])

    def _remove(self, key):
        """Removes node with given data. Raises KeyError if data is not in list."""

        node, update = self._scan(key)
        if not node:
            raise KeyError

        with update.lock():
            for level in range(len(node.nxt)):
                update[level].nxt[level] = node.nxt[level]

            # trim not used head
            for i in reversed(range(len(self.head.cnt))):
                if self.head.cnt[i] == self.tail:
                    head_node = self.head.cnt.pop()
                    del head_node
                else:
                    break

        del node


class Skiplist(SkiplistAbstractBase, collections.MutableMapping):

    def _remove(self, key):
        super(Skiplist, self)._remove(key)
        self._size -= 1

    def _insert(self, key, data):
        super(Skiplist, self)._insert(key, data)
        self._size += 1

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    def __init__(self, **kwargs):
        super(Skiplist, self).__init__()

        self._tail = _Skipnode(NIL(), None, [], [])
        self._head = _Skipnode(None, 'HEAD', [self.tail], [])
        self._tail.prev.extend([self.head])

        self._size = 0

        for k, v in kwargs.items():
            self[k] = v

    def __len__(self):
        return self._size

    def __str__(self):
        return 'skiplist({{{}}})'.format(
            ', '.join('{key}: {value}'.format(key=node.key, value=node.data) for node in self._level())
        )

    def __getitem__(self, key):
        """Returns item with given index"""
        node, _ = self._scan(key)
        if node is None:
            raise KeyError('Key <{0}> not found'.format(key))
        return node.data

    def __setitem__(self, key, value):
        return self._insert(key, value)

    def __delitem__(self, key):
        self._remove(key)

    def __iter__(self):
        """Iterate over keys in sorted order"""
        return (node.key for node in self._level())

    def iteritems(self):
        return ((node.key, node.data) for node in self._level())

    def iterkeys(self):
        return (item[0] for item in self.iteritems())

    def itervalues(self):
        return (item[1] for item in self.iteritems())

if __name__ == '__main__':
    s = Skiplist()
    for i in range(100):
        s[random.randrange(1, 1000)] = random.randrange(1, 1000)

    k = list(s.keys())
    assert k == sorted(k)

