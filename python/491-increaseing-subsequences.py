#/usr/bin/env python
#encoding: utf-8

'''
https://leetcode.com/problems/increasing-subsequences/description/

- 递增的搜索树，想到用dfs，可以画树来辅助理解
- 用一个vector来记录当前的访问路径（前置集合）
- 每一次进入到dfs，就是一次记录点
- 这里题目的要求，需要判重（不是很理解，不过细节不追究了）

- 另外一个非常好的方法是集合方法，每一次访问最新元素，都是和当前集合合并。
- 注意初始的时候空集非常重要，用来初始化最开始的元素。
- 效率反而由于dfs，毕竟递归是有小
'''
class Solution:
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def dfs(buffer, nums, start):
            if len(buffer) > 1:
                res.append(buffer[:])

            unique = set()
            for i in range(start, len(nums)):
                if i > 0 and nums[i] in unique:
                    continue

                if not buffer or buffer[-1] <= nums[i]:
                    unique.add(nums[i])
                    buffer.append(nums[i])
                    dfs(buffer, nums, i+1)
                    buffer.pop()

        dfs([], nums, 0)
        return res

    def findSubsequences_using_set(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 注意初始的时候有一个空集合
        res = {()}
        for v in nums:
            res |= {sub_set + (v, ) for sub_set in res if not sub_set or v>=sub_set[-1]}
        return [list(v) for v in res if len(v) >= 2]
