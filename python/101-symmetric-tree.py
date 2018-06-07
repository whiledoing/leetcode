#/usr/bin/env python
#encoding: utf-8

'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
'''

'''
看似很简单，但是自己想确实有想不出来。

- 看似是对root进行分析，其实是对两个子树进行比较，因为访问的时候需要同时对比两个子树内容，所以其实是对两个树进行递归。
- 这里递归主要是判断中心节点是否相同，如果相同，就递归判断子节点。子节点有意思在于，将A的左节点和B的右节点比较（分析时候可以直接分析到叶子节点层面，便于思考）
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self._impl(root.left, root.right)

    def _impl(self, t1, t2):
        if not t1 and not t2: return True
        if not t1 or not t2: return False
        if t1.val != t2.val: return False
        return self._impl(t1.left, t2.right) and self._impl(t1.right, t2.left)