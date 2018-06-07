#/usr/bin/env python
#encoding: utf-8

"""
很巧妙的方法

- 每一次排列等于自己排好，然后让后面的内容进行排列
- 通过swap，每一次都将当前数字放到dfs的第一层
- 运算到最后，得到最终结果
"""

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def dfs(nums, start):
            if start >= len(nums):
                res.append(nums.copy())
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                dfs(nums, start+ 1)
                nums[start], nums[i] = nums[i], nums[start]

        dfs(nums, 0)
        return res