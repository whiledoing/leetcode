#/usr/bin/env python
#encoding: utf-8

'''
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.

分析这里的递归：

- 每次计算左边最长路径 + 右边最长路径
- 如果将递归设定为，计算每一个子节点的最长路径（连接左右和中间基恩点）），那么到上一层就没有办法选择具体用子节点的哪一个路径。
- 将dfs设定为计算**每个节点上最长的节点长度**
- 而用一个全局变量在后序遍历过程中，统计目前遍历所遇到的最长长度。
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0

        def depth(p):
            if not p: return 0
            left, right = depth(p.left), depth(p.right)
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)

        depth(root)
        return self.ans