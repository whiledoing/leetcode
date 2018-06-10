#/usr/bin/env python
#encoding: utf-8

"""
Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n2) is trivial. You MUST do better than that.

Example:

Input: nums = [-2,5,-1], lower = -2, upper = 2,
Output: 3
Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.

- 第一步是将区间和变成accumulate的两数相减
- 如果去掉范围，只是考虑单边条件，比如只考虑大于upper，是不是就变成了reverse pair类似的问题，只是这里我们是对accumulatem的数据进行分析。
- 从左到右搜索时，可以用balanced BST记录已经扫描过的accumulate数值。
- 当然这种reverse pair问题都可以用merge sort方法，因为merge sort在搜索符合特定差值问题时，可以**线性搜索**（因为有序）

wrap:

- 范围差都可以转化为accumulate两个数值的差。
- 范围的概念就想到reverse pair的问题模型，因为A[j] - A[i] 需要 j > i，就天然想到了merge sort的归并过程。
- 数组问题都可以想到divide and conquer的思路。
- 双边问题可以变成单边问题
"""


class Solution:
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        n = len(nums)
        buffer = [0] * (n+1)

        # 实现时候这个注意，需要加入初始节点0，这样子accu[i] - accu[0] 才表示 [0-i]的求和。
        accu = [0]
        for v in nums:
            accu.append(accu[-1] + v)

        def merge_sort(l, r):
            if l >= r: return 0
            m = l + ((r - l) >> 1)
            res = merge_sort(l, m) + merge_sort(m + 1, r)

            # p和q分别表示左右边界，p的任务是找到第一个符合要求的下限，而q的任务是第一个超过upper的上限
            # 所以将i作为开始节点的区间个数为 `q-p`
            i, j, p, q, k = l, m + 1, m + 1, m + 1, 0
            while i <= m:
                while p <= r and nums[p] - nums[i] < lower: p += 1
                while q <= r and nums[q] - nums[i] <= upper: q += 1
                res += q - p

                while j <= r and nums[i] > nums[j]:
                    buffer[k], k, j = nums[j], k + 1, j + 1
                buffer[k], k, i = nums[i], k + 1, i + 1

            # 更高效，因为后面的不需要计算
            nums[l:l + k] = buffer[:k]
            return res

        return merge_sort(0, n)
