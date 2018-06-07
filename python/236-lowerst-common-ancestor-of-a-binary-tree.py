#/usr/bin/env python
#encoding: utf-8

"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

Given the following binary search tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4

Example 1:

Input: root, p = 5, q = 1
Output: 3
Explanation: The LCA of of nodes 5 and 1 is 3.

Example 2:

Input: root, p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself
             according to the LCA definition.


- 这个题目的递归非常有意思，也很绕脑子。
- 递归计算的是当前子节点下面是否存在p和q的公共子节点，如果存在就自下而上返回。
- 如果只有一边有，那么公共子节点就是有的那一侧
- 如果两边都有，非常有意思，说明到这一层之前并没有找到对应的公共子节点（考虑自下而上），那么root就是公共子节点。
- 递归分析：输入两个数值，递归可以返回一个数值，该数值在最后合并的时候推演出公共的概念！非常有意思的题目！

还有一种方式使用先序遍历的方式

- 先序遍历，先返回root节点，在左右。之所以这样子是因为遍历的时候反向保存了叶子到root的关系。
- 一旦两个节点都找到，停止遍历
- 根据反向映射得到节点，其实还有一个方法是转变为链表，然后计算两个链表的交点。
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution(object):
    # def lowestCommonAncestor(self, root, p, q):
    #     """
    #     :type root: TreeNode
    #     :type p: TreeNode
    #     :type q: TreeNode
    #     :rtype: TreeNode
    #     """
    #     if root in (None, p, q): return root
    #     left, right = (self.lowestCommonAncestor(kid, p, q) for kid in (root.left, root.right))
    #     return root if left and right else left or right

    # def lowestCommonAncestor_iterative(self, root, p, q):
    #     stack = [root]
    #     parent = {root: None}
    #     while p not in parent or q not in parent:
    #         node = stack.pop()
    #         if node.left:
    #             parent[node.left] = node
    #             stack.append(node.left)
    #         if node.right:
    #             parent[node.right] = node
    #             stack.append(node.right)
    #     ancestors = set()
    #     while p:
    #         ancestors.add(p)
    #         p = parent[p]
    #     while q not in ancestors:
    #         q = parent[q]
    #     return q

class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        n = len(N)
        dp_1 = [[0]*n for _ in range(n)]
        dp_2 = [[0]*n for _ in range(n)]
        res = 0

        mines_m = {(x, y):True for x, y in mines}
        for i in range(n):
            for j in range(n):
                if (i,j) in mines_m:
                    dp_1[i][j] = 0
                elif j == 0:
                    dp_1[i][j] = 1
                else:
                    dp_1[i][j] = min(dp_1[i][j-1], dp_1[i-1][j])+1

        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if (i,j) in mines_m:
                    dp_2[i][j] = 0
                elif j == n-1:
                    dp_2[i][j] = 1
                else:
                    dp_2[i][j] = min(dp_2[i][j+1], dp_2[i+1][j])+1

        for i in range(n):
            for j in range(n):
                res = max(res, min(dp_1[i][j], dp_2[i][j]))