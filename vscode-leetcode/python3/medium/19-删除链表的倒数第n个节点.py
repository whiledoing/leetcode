#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#
# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (36.81%)
# Likes:    633
# Dislikes: 0
# Total Accepted:    103.9K
# Total Submissions: 282.2K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
#
#
# 说明：
#
# 给定的 n 保证是有效的。
#
# 进阶：
#
# 你能尝试使用一趟扫描实现吗？
#
#

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 这里好的方法是加一个 Dummy 的节点，开始都指向 dummy 节点，然后最后再获取到 dummy 的 next 即可。
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n <= 0: return head

        i, p, q = n, head, head
        while i and q: i, q = i-1, q.next
        if not q: return None if i else head.next

        while p and q: last_p, p, q = p, p.next, q.next
        last_p.next = p.next
        return head


# @lc code=end

def make_list(v):
    if not v: return None
    node = ListNode(v[0])
    node.next = make_list(v[1:])
    return node

def print_list(head):
    while head:
        print(head.val, '', end='')
        head = head.next
    print()

head = make_list([1,2])
print_list(Solution().removeNthFromEnd(head, 2))
