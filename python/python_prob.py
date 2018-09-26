#/usr/bin/env python
#encoding: utf-8

class LinkedNode:
    __slots__ = 'value', 'next'

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class AccessOrderedDict(object):
    """使用单向链表和**前置节点字典**实现类似LRU的特殊字典，用来记录最早被修改的数据。

    使用前置节点字典的实现方式相比于双向链表实现方法更省内存。（否则链表变为双向链表）
    """
    def __init__(self):
        # sentinel
        self.head = LinkedNode()
        self.tail = None
        self.node_pre_map = {}

    def __setitem__(self, k, v):
        # 已经存在，将前置节点取出，设置关系
        if k in self.node_pre_map:
            pre = self.node_pre_map.pop(k)
            pre.next, cur = pre.next.next, pre.next
            if not cur.next: self.tail = pre
        else:
            cur = LinkedNode()

        # 将节点插入到链表头部
        self._insert_into_front_impl(cur, (k, v))

    def _insert_into_front_impl(self, node, new_value):
        node.value = new_value
        node.next = self.head.next
        self.head.next = node
        self.node_pre_map[node.value[0]] = self.head

        if node.next:
            self.node_pre_map[node.next.value[0]] = node
        else:
            self.tail = node

    def get_least_used_value(self):
        """得到最早被访问的数据"""
        return self.tail.value[1] if self.tail else None

    def __len__(self):
        return len(self.node_pre_map)


def find_min_length_sub_array_contain_all_equal_nums_use_ordered_dict(nums):
    """得到数组中包含所有元素最短子序列的长度

    实现说明：

    - 使用set统计唯一元素个数
    - 从左到右遍历数据，使用`AccessOrderedDict`记录元素v的最大坐标。
    - 如果已经统计到所有的唯一元素，将当前`AccessOrderedDict`中最小的元素坐标取出，计算区间长度，并统计最小值。
    - 因为每次插入到字典中的数据都是当前的坐标最大值，所以字典中最早被访问到的数据就是最小值。

    时间复杂度 && 空间复杂度：O(n)

    >>> find_min_length_sub_array_contain_all_equal_nums_use_ordered_dict([1, 8, 8, 8, 1])
    2
    >>> find_min_length_sub_array_contain_all_equal_nums_use_ordered_dict([2, 8, 8, 8, 1, 1])
    5
    >>> find_min_length_sub_array_contain_all_equal_nums_use_ordered_dict([1, 1, 1, 1, 1, 1])
    1
    >>> find_min_length_sub_array_contain_all_equal_nums_use_ordered_dict([1, 2, 2, 2, 2, 8])
    6
    >>> find_min_length_sub_array_contain_all_equal_nums_use_ordered_dict([8, 2, 2, 2, 1, 8])
    3
    """
    if not nums: return 0
    res, unique_len = len(nums), len(set(nums))

    # 统计元素的最大下标
    max_index_map = AccessOrderedDict()

    for i, v in enumerate(nums):
        max_index_map[v] = i
        if len(max_index_map) < unique_len: continue

        # 最久远被访问的数据，就是当前坐标最小值
        min_index = max_index_map.get_least_used_value()
        res = min(res, i-min_index+1)

    return res


if __name__ == '__main__':
    import doctest
    doctest.testmod()

