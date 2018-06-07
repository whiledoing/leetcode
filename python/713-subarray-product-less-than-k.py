#/usr/bin/env python
#encoding: utf-8

"""
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.

第一种解法：

- 看到连续相乘，考虑使用区间累积的概念。
- 用log将乘变为加法，然后进行区间累积。
- 每次遍历用二分找到上限（bisect_right）计算的到范围

第二种解放，滑动窗口：

- 连续的概念可以考虑滑动窗口，如果每次遍历right的时候可以有效的计算left的位置
- 这里刚好可以，因为是连续乘的概念，所以将left不停移动，直到小于K为止。
- **窗口的大小就是个数**，这个其实也非常VIP
"""


class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import math, bisect
        if k == 0: return 0
        k = math.log(k)

        # 乘积可能太大，将乘变成加法，使用log运算
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + math.log(x))

        # 每次计算下一个位置，因为数据递增，所以用二分搜索
        ans = 0
        for i, x in enumerate(prefix):
            j = bisect.bisect(prefix, x + k - 1e-9, i + 1)
            ans += j - i - 1
        return ans

    def numSubarrayProductLessThanK_using_sliding_window(self, nums, k):
        if k <= 1: return 0

        # 遍历的位置记做right，每一次滑动窗口，如果乘积过大，那么缩小left的范围。
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans