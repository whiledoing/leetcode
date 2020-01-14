'''
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

    Each of the array element will not exceed 100.
    The array size will not exceed 200.

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.

- 分解两个集合，其实等于**分解一个集合的特定值**，因为一旦分解开了，另外一个就解决了
- 考虑使用dfs和mem方法更快，因为dfs只解决一个目标。
- 当然这里也可以使用dp，dp实现的时候有一个tricky，因为每次dp的指针交换，所以不需要重复刷新的地方可以直接通过交换得到数值。
- 另外一个是copy过来的，直接使用一行的set代码，很有意思。
'''

class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_v = sum(nums)
        if sum_v & 1: return False
        mem = {}
        def dfs(nums, n, s):
            if n < 0: return False
            if s == 0: return True
            if s < 0: return False
            if (n, s) in mem: return mem[(n, s)]
            mem[(n, s)] = dfs(nums, n-1, s-nums[n]) or dfs(nums, n-1, s)
            return mem[(n, s)]

        return dfs(nums, len(nums)-1, sum_v//2)

    def canPartition_using_set(self, nums):
        """tricky"""
        from functools import reduce
        return (sum(nums) / 2.) in reduce(lambda cur, x: cur | {v + x for v in cur}, nums, {0})

    def canPartition_use_backtracking(self, nums):
        sum_v = sum(nums)
        if sum_v & 1: return False

        def dfs(s, t):
            if t == 0: return True
            for v in nums[s:]:
                if dfs(s+1, t-v):
                    return True
            return False

        return dfs(0, sum_v >> 1)

    def canPartition_using_dp(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_v = sum(nums)
        if sum_v & 1: return False
        sum_v = sum_v//2

        dp = [[False]*(sum_v+1), [False]*(sum_v+1)]
        dp[0][0], dp[1][0] = True, True

        for v in nums:
            # tricky part, we don't need to write like:
            # dp[0][j] = dp[1][j]
            # if j>=v: dp[0][j] |= dp[1][j]
            #
            # because we resue dp[0] as dp[1] end of the loop, so we resue the same value before v
            for j in range(v, sum_v+1):
                dp[0][j] = dp[1][j] or dp[1][j-v]
            dp[0], dp[1] = dp[1], dp[0]

        return dp[0][sum_v]

if __name__ == "__main__":
    print(Solution().canPartition_use_backtracking([1, 5, 11, 5]))
    print(Solution().canPartition_use_backtracking([1, 2, 3, 5]))