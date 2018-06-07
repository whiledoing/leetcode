#/usr/bin/env python
#encoding: utf-8

'''
写法非常精悍。

- 用一个dummy节点表示头，这样子不需要初始化，最后再返回dummy.next
- 交换的方式得到当前最小的节点
- l1 or l2的方式得到有效的链表
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur = head = ListNode(None)
        while l1 and l2:
            if l2.val < l1.val: l1,l2=l2,l1
            cur.next = l1
            cur = cur.next
            l1 = l1.next
        cur.next = l1 or l2
        return head.next