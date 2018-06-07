#/usr/bin/env python
#encoding: utf-8

"""
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.

- 本质上还是搜索问题，使用dfs进行搜索。
- 放置问题可以抽象为对每一个数值遍历放置在K个可能的盒子中。
- 剪枝优化：1）如果存在数据大于平均值，False 2）从大到小放置，这样子减少了搜索空间 3）等价性。如果前面放置了一个空盒子, 后面还有空盒子不需要放置，等价的搜索。
"""
class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums = sorted(nums, reverse=True)
        sum_v = sum(nums)
        if sum_v % k: return False
        sum_v /= k
        bucket = [0] * k

        # 如果存在任何一个数据大于平均值，直接返回，优化
        if any(True for v in nums if v > sum_v): return False

        # dfs搜索，这里不同于backtracking，不存在不放的情况，只是说要将数据放到哪个盒子中
        # 优先放置大数据，这样子很容易开始的盒子就不可以放置，大大的剪枝
        self.found = False
        def dfs(nums, s, sum_v):
            if self.found:
                return True

            if s >= len(nums):
                self.found = True
                return True

            empty_bucket_has_put_value = False
            for i, v in enumerate(bucket):
                # 如果盒子放不进去，剪枝，不计算该盒子，所以从大到小计算
                if nums[s] + v > sum_v: continue

                # vip, 如果没有放过数据，且之前放过空数据，那么不放置，状态重复
                if v == 0 and empty_bucket_has_put_value: break
                if v == 0: empty_bucket_has_put_value = True
                bucket[i] += nums[s]
                dfs(nums, s+1, sum_v)
                bucket[i] -= nums[s]

        dfs(nums, 0, sum_v)
        return self.found