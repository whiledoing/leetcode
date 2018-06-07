#/usr/bin/env python
#encoding: utf-8
'''
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2

Note:

    The length of the array is in range [1, 20,000].
    The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

- 看到求区间和，想到**累加子字段**和，这样子两个区间和就是区间差。
- 现在唯一问题是，计算到i节点时，需要之前的区间中有多少等于特定数值（相减为K）
- 所以想到用字段缓存之前计算得到的和值，而且可以一次性的run得到结果。
'''

class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res, sum_v, sum_d = 0, 0, {0:1}
        for v in nums:
            sum_v += v
            res += sum_d.get(sum_v-k, 0)
            sum_d[sum_v] = sum_d.get(sum_v, 0) + 1
        return res