#/usr/bin/env python3
#encoding: utf-8

'''
实现的非常漂亮：

- 将节点抽象为prev，head
- 记录next，这样子设置head的next之后，原来的next找不到了
- 将第一次的过程放入到prev中，这样子不需要写额外的逻辑。也正因为如此，所以设置prev，表示前置节点

另外，使用尾递归的写法，非常漂亮：

https://leetcode-cn.com/problems/reverse-linked-list/solution/python-1xing-wei-di-gui-3xing-die-dai-by-knifezhu/#comment
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev, head = head, next
        return prev

    def reverseList(self, head: ListNode, tail: ListNode = None) -> ListNode:
        if head: head.next, tail, head = tail, head, head.next
        return self.reverseList(head, tail) if head else tail
