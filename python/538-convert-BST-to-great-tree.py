#/usr/bin/env python
#encoding: utf-8
'''
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
'''

'''
- 首先考虑遍历顺序是右序，就是右-中-左
- dfs遍历时可通过返回值传递有效信息，不一定一定是TreeNode（构建树时用到），也可以是某一个遍历过程中的中间数值。
- 考虑简单过程：1）遍历得到右侧所有数据之和 2）中值加入右侧数据和 3）遍历左侧 4）返回所有元素之和
- 再进一步：1）右遍历返回值加到中值 2）左侧遍历结束之后返回值记为总体返回值
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(root, init_v):
            if not root: return init_v
            root.val += dfs(root.right, init_v)
            return dfs(root.left, root.val)

        dfs(root, 0)
        return root
