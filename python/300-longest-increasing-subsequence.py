'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

这个题目可以使用DP，时间复杂度为O(n)，这个算法非常的神奇，要非常仔细理解才可以想的清楚

- 如果数据递增，将数据放到最后一位。
- 将数据二分查找（左插入）进行替换。
- 最后dp的长度就是最后数组的长度。
'''

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import bisect
        dp = []
        for v in nums:
            #insert_index = self.bisect_left(dp, v)
            insert_index = bisect.bisect_left(dp, v)
            if insert_index == len(dp):
                dp.append(v)
            else:
                dp[insert_index] = v
        return len(dp)

    def bisect_left(self, data, v):
        # @note 这里实现的非常tricky，使用len(data)可以计算出最后一个节点。
        left, right = 0, len(data)
        while left < right:
            mid = (left+right)//2
            if v <= data[mid]:
                right = mid
            else:
                left = mid+1
        return right