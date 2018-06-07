#/usr/bin/env python
#encoding: utf-8

"""
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.

- 本质上类似于背包问题，只是要抽象出一个二维的dp结构
- 取了一个数（这里是位置，也就可以计算得到一个数，区间累积和），等于后面取m-1个数的最优值和当前比较，得到当前的最优值
- 所以两个维度，一个是个数，一个是位置。
- 经常想到是否是dp结构的问题。

- 另外，最好的方法是通过二分搜索，从值域的角度考虑。可能的数值在[max(nums), sum(nums)]之间，通过二分进行搜索。
- 如果取得一个数值，去进行nums的划分，如果划分出来的个数多于m，说明数值较小，left = mid+1。否则, right=mid
- 问题一般人想不到这个解法。不过经验就是：可以从数值的角度来进行划分。如果有最大和最小可能数值，通过二分定位是一个非常好的方法。
"""

class Solution:
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        from itertools import accumulate
        from sys import maxsize
        n, A, memo = len(nums), list(accumulate(nums)), {}

        # 明确这是一个2维问题，一个维度是阶段m，一个是开始位置s
        # 用dfs使用维度内容作为memo的坐标
        # 将nums[0]做为底运算更方便。这里的s表示从0到s的所有字符串，这比将nums[n-1]做为底方便，因为dfs时只需要和0进行比较即可。
        # 将nums[0]做为底还有一个好处，就是更方便得到初始值(m==1)，因为这就是accumulate计算的结果。
        # 实现的时候，使用reversed逻辑更简洁
        def dfs(s, m):
            if m == 1: return A[s]
            if (s, m) in memo: return memo[(s, m)]

            # 这里的dfs实现类似backtracking，等价于切的第一刀就是第一次取的节点，后面的dfs再分析。等价于取数问题，前面都不取，就取了
            # 这一个节点。
            min_v, sum_v = maxsize, 0
            for i in reversed(range(m-1, s+1)):
                # 非常好的优化，如果当前的累加值超过了最小值，那么再计算也不会超过最小值
                # 因为是取得最大值之后的最小值，如果sum比最小值大，那么最大值至少大于等于sum，那么不影响结果
                sum_v += nums[i]
                if sum_v >= min_v: break
                min_v = min(max(sum_v, dfs(i-1, m-1)), min_v)
            memo[(s, m)] = min_v
            return min_v

        return dfs(n-1, m)

    def splitArray_dp(self, nums, m):
        from itertools import accumulate
        n, dp = len(nums), list(accumulate(nums))

        # dp的实现也非常简洁，同样也是将nums[0]做为底节点，这样子初始dp就是accumulate的结果
        # dp[s][i] = min(max(dp[s-1][for all j in reversed(range(0, i))], sum[i to j]))
        for s in range(2, m+1):
            for i in reversed(range(s-1, n)):
                sum_v = nums[i]
                for j in reversed(range(0, i)):
                    if sum_v >= dp[i]: break
                    dp[i] = min(dp[i], max(dp[j], sum_v))
                    sum_v += nums[j]

        return dp[-1]