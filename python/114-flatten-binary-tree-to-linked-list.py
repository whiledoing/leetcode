#/usr/bin/env python
#encoding: utf-8

"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6

The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6


- 输出的数据从下面到上面看（因为dfs是最下面开始输出），明显可以看到，遍历顺序是 右-中-左
- 所以按照 右-中-左 进行遍历，访问的节点记做prev，这样子回去时候设置右节点为prev即可
- 数的问题，考虑到树的遍历角度进行分析。
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        self.prev = None
        def dfs(root):
            if not root: return None
            dfs(root.right)
            dfs(root.left)
            root.right = self.prev
            root.left = None
            self.prev = root
        dfs(root)