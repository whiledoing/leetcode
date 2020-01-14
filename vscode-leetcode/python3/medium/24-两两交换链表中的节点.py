#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (63.48%)
# Likes:    370
# Dislikes: 0
# Total Accepted:    61.1K
# Total Submissions: 96.2K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#
# 示例:
#
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
#
#
#

from utils import *

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head: return None
        p, q = head, head.next
        pp, pp.next = self, head
        while p and q:
            pp.next, p.next, q.next, pp, p, q = q, q.next, p, p, q.next, q.next.next if q.next else None
        return self.next

        # 这里用 pre 表示前置节点，然后判断两个后置节点存在来进行循环展开，代码更加精简一些
        # while pre.next and pre.next.next: pass
        # 因为这样子，后续 p q 两个节点next 的时候，不需要再分开检测了。

# @lc code=end

head = make_list([1,2,3,4])
print_list(Solution().swapPairs(head))
