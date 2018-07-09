"""
Given a binary tree rooted at root, the depth of each node is the shortest distance to the root.

A node is deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is that node, plus the set of all descendants of that node.

Return the node with the largest depth such that it contains all the deepest nodes in it's subtree.



Example 1:

Input: [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation:



We return the node with value 2, colored in yellow in the diagram.
The nodes colored in blue are the deepest nodes of the tree.
The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the given tree.
The output "[2, 7, 4]" is a serialization of the subtree rooted at the node with value 2.
Both the input and output have TreeNode type.

递归的想法其实并不容易想到：

- 如果左子树深度大，那么包含所以最深节点的子树肯定在左边
- 计算dfs的时候，同时计算深度。
- 如果两个子树的深度相同，返回root本身。因为是dfs，所以自下而上计算，第一个计算得到的就是结果，同时自下而上保存
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(root):
            # 返回两个元素：（当前树深度，subtreeWithAllDeepest）
            if not root: return 0, None
            l, r = dfs(root.left), dfs(root.right)
            return max(l[0], r[0])+1, root if l[0]==r[0] else l[1] if l[0] > r[0] else r[1]
        return dfs(root)[1]

    def subtreeWithAllDeepest_no_dfs(self, root):
        """
        no_dfs的方法就是两次扫描，找到第一个节点
        """
        if not root: return root
        par = {}
        q = [root]
        while True:
            new_q = []
            for v in q:
                if v.left:
                    new_q.append(v.left)
                    par[v.left] = v

                if v.right:
                    new_q.append(v.right)
                    par[v.right] = v

            if not new_q: break
            q = new_q

        q = set(q)
        while len(q) > 1:
            q = {par[v] for v in q}
        return next(iter(q))