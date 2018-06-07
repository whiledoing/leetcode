#/usr/bin/env python
#encoding: utf-8

'''
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

     3
    / \
   2   3
    \   \
     3   1

Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Example 2:

     3
    / \
   4   5
  / \   \
 1   3   1

Maximum amount of money the thief can rob = 4 + 5 = 9.

- 首先想到这是一个递归问题，当前的结果可以根据子结构进行计算。
- 递归考虑两个问题：1）结束条件 2）推演管理
- 结束条件好理解，空节点时候返回0，没有办法抢劫。
- 推演考虑两个维度，一个是当前节点是否被抢，如果被抢劫，子节点不能被抢劫。如果没有，就等于子节点可以得到的最大值。
- 所以将dfs返回两个数值，一个表示被抢劫，一个没有
- dfs还要想到一个问题，是否存在重复计算，这里明显是有的，使用mem方式。

- 加快速度可以手写递归，使用后续遍历结合mem方式。（当前结果依赖于子节点计算完成）
- 自底向上的方式，一定程度上也提高了速度
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        mem = {}
        def dfs(root):
            if not root: return (0, 0)
            if root in mem: return mem[root]
            left, right = dfs(root.left), dfs(root.right)
            take = left[1] + right[1] + root.val

            # key here: if not take, I don't care whether child node be robbered
            not_take = max(left) + max(right)

            mem[root] = (take, not_take)
            return mem[root]

        return max(dfs(root))

    def rob_with_post_travel(self, root):
        stack = [(0, root)]
        d = {None: (0, 0)}
        while stack:
            seen, node = stack.pop()
            if node is None:
                continue
            if not seen:
                stack.extend([(1, node), (0, node.right), (0, node.left)])
            else:
                yesrob = d[node.left][1] + d[node.right][1] + node.val
                norob = max(d[node.left]) + max(d[node.right])
                d[node] = (yesrob, norob)
        return max(d[root])