#/usr/bin/env python
#encoding: utf-8

"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example:

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

- 使用层序遍历树存在一个问题，如果某一个子树很早就结束了(都是None)， 但为了保存层级信息，后面层级必须还输出None，数据严重冗余
- 另一种方式使用pre-order和结束符方法可以dfs解析数据。
- 反序列化时，用iter更方便，因为每次只吸收一个数据。
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                # @key 使用结束符标识结束状态
                vals.append('#')
        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node

        # 使用iter更加方便，每次消耗一个数据，不需要维护索引
        vals = iter(data.split())
        return doit()

    def level_serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''
        res = [str(root.val)]
        q = [root]

        while q:
            new_q = []
            has_not_null = False
            for v in q:
                left_node = v.left if v else v
                new_q.append(left_node)

                right_node = v.right if v else v
                new_q.append(right_node)

                has_not_null |= bool(left_node)
                has_not_null |= bool(right_node)

            if not has_not_null: break
            q = new_q
            res.extend(str(v.val) if v else 'None' for v in q)

        return ','.join(res)

    def level_deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        data = data.split(',')

        def make_node(i):
            if i >= len(data): return None
            if data[i] == 'None': return None
            return TreeNode(int(data[i]))

        root = make_node(0)
        q = [root]
        i = 1
        while q:
            new_q = []
            for node in q:
                left_node, i = make_node(i), i + 1
                new_q.append(left_node)
                if node: node.left = left_node

                right_node, i = make_node(i), i + 1
                new_q.append(right_node)
                if node: node.right = right_node

            if i >= len(data): break
            q = new_q
        return root