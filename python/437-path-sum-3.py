#/usr/bin/env python
#encoding: utf-8

'''
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root: return 0

        def dfs(root, sum):
            if not root: return 0
            return (root.val == sum) + dfs(root.left, sum - root.val) + dfs(root.right, sum - root.val)

        # 两个部分：1）一个部分计算当前树所有路径之后 2）另外一个dfs计算通过通过当前头节点的通路数目（注意，该情况，每一个节点都必须被计算进去）
        return dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    d = {'(': ')', '{': '}', '[': ']'}
    buff = []
    for c in s:
        if c in d:
            buff.append(d[c])
        else:
            if buff[-1] != c:
                return False
            buff.pop()

    print('buff is %r' % buff)
    return not buff

if __name__ == '__main__':
    isValid('()')