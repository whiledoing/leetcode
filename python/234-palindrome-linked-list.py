#/usr/bin/env python
#encoding: utf-8

'''
非常巧妙的实现和非常好的实现方式

- 回文想到对称
- 使用fast和slow的方式得到链表的middle属性
- 使用pre和cur的方式进行链表反转
- 然后变成检查是否两个链表相同的逻辑
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 使用fast快速到终点，而slow得到中点
        pre, slow, fast = None, head, head
        while fast and fast.next:
            fast = fast.next.next
            pre, pre.next, slow = slow, pre, slow.next

        # 如果是奇数，中间点不比较
        if fast:
            slow = slow.next

        # 向前计算一个节点，这样子可以反向将链表还原，使用p_pre的方式和pre进行配合还原
        # 注意特殊情况，如果两个都无效，也是有效的回文，而一个无效，不是有效回文。
        if not pre or not slow: return pre == slow
        if pre.val != slow.val: return False

        # 一边next，一边将节点重新组织
        p_pre, pre, slow = pre, pre.next, slow.next
        while pre and slow and pre.val == slow.val:
            pre.next, pre, p_pre, slow = p_pre, pre.next, pre, slow.next
        return not pre and not slow

