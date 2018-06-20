#/usr/bin/env python
#encoding: utf-8

"""
In a given integer array A, we must move every element of A to either list B or list C. (B and C initially start empty.)

Return true if and only if after such a move, it is possible that the average value of B is equal to the average value of C, and B and C are both non-empty.

Example :
Input:
[1,2,3,4,5,6,7,8]
Output: true
Explanation: We can split the array into [1,4,5,8] and [2,3,6,7], and both of them have the average of 4.5.
Note:

The length of A will be in the range [1, 30].
A[i] will be in the range of [0, 10000].

实现参考代码：https://leetcode.com/problems/split-array-with-same-average/discuss/120667/C++-Solution-with-explanation-early-termination-(Updated-for-new-test-case)

- 首先，这个题目是NP问题，不存在线性N的时间
- 如果直接使用搜索，会退化为指数复杂度，不可取。
- 这里用到了平均数的特性，如果分割的两个部分均值相同，那么存在k个数的和为sum(A)*k/n
- 为了找到所有k个数和值集合，使用dp，每一次主循环取得一个新的数字来刷新当前和值集合，计算时，
注意刷新集合的方向不可以反。
- 之所以使用set而不是dp[sum]，是因为set内存更好，如果使用hash-set，那么时间复杂度也可以忽略不计。
- 时间复杂度为O(n^2*m*log(n*m))，其中m为单个数值的范围。在值域可控的时候，该算法比指数复杂度
要快的多的多。每一次遍历，需要对最多n*m个数据进行update计算（考虑n个数可能构成的值域范围），同时log(n*m)时间
进行set计算，当然如果用hash-map，就不需要该log时间。
- 如果值域可控，考虑从值域角度分析数据
"""

def splitArraySameAverage(A):
    # 这里用到了平均数的特性，如果分层两个部分的均值相同，那么存在i个数的和为sum(A)*i/n
    n, m, t_sum = len(A), len(A)//2, sum(A)
    if all(t_sum*i%n != 0 for i in range(1, m+1)): return False

    # 用set来记录可能的sum元素个数，这样子比直接用dp[sum]来记录，更节省内存（如果sum个数稀疏的话）
    # 额外的代价就是用set或者map记录sum的个数，但这基本上也比直接用dp[sum]来记录方便。
    sum_set = [set() for _ in range(m+1)]
    sum_set[0].add(0)

    # 这里留意在于，需要反向运算sum_set。因为每一次新加入一个元素num来刷新当前结果，都是将上一次
    # i-1个数记录结果来推导i个数的结果，如果正向计算，会导致计算重复计算，可以画图仔细想一想。
    for num in A:
        for i in range(m, 0, -1):
            sum_set[i].update({v+num for v in sum_set[i-1]})

    # 使用any极大提高代码的可读性，值得推荐
    return any(t_sum*i % n == 0 and (t_sum*i/n) in sum_set[i] for i in range(1, m+1))

def splitArraySameAverage_with_dfs(A):
    n, m, t_sum = len(A), len(A)//2, sum(A)

    # 从小到大排序，从尾巴开始遍历，这样子从最大的开始结算效果更好
    A = sorted(A)
    def exists(idx, k, tar):
        # 结束条件
        if k == 0: return tar == 0

        # 判断数据是否太小，如果当前tar巨大，而后面的数据（越后面越小）不满足要求剪枝
        if A[idx]*k < tar: return False

        # backtracking: 从尾巴开始取数据，最迟从k个数位置开始（否则无效），取得数据后，判断当前tar是否
        # 太小，如果太小，取了数据就负数了。这里有两个剪枝
        return any(A[i] <= tar and exists(i-1, k-1, tar-A[i]) for i in range(idx, k-2, -1))

    # 使用dfs相比于dp，在平均时间复杂度上会更好，因为dfs只计算一个分支，并不需要计算所有结果
    # 但dfs快于dp的先决条件是**剪枝会成功**，如果剪枝不成功，会退化为**指数时间复杂度**，所以效果并不好
    return any(t_sum*i % n == 0 and exists(n-1, i, t_sum*i/n) for i in range(1, m+1))