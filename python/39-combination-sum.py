#/usr/bin/env python
#encoding: utf-8

"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

- 这种写法叫做backtracking，对于取数据，一个或多个，对于取集合非常好用
- 其递归的方式是，比如考虑ABC三个数据，先取A然后递归，然后不取A，取B，且不考虑A的递归，然后不考虑A和B，只考虑C的递归
- 每一次递归有一些列的平级递归产生。
- 对于是否取数，可以控制dfs的start参数。
- 重复性可以参考下面第二段代码的说明。
"""

class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        res, buffer, n = [], [], len(candidates)

        # d表示数据，s表示开始坐标，n表示结束坐标，t表示目标
        def dfs(d, s, n, t):
            if not t:
                res.append(buffer.copy())
                return

            # 剪枝，如果当前目标过小，没有东西放了，直接返回
            # 这种递归方式写起来更方便，对于permutation，combination问题特别好用
            for i in range(s, n):
                if t<d[i]: break
                buffer.append(d[i])
                dfs(d, i, n, t-d[i])
                buffer.pop()

        dfs(candidates, 0, n, target)
        return res

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res, buffer, n, candidates = [], [], len(candidates), sorted(candidates)

        def dfs(d, s, n, t):
            if not t:
                res.append(buffer.copy())
                return

            # 这里不一样，如果相连接元素相同，不计算。
            # 因为这里逻辑表示：取当前i元素，不取之前元素的情况
            # 如果前一个i取了，经过dfs，那么等价于后面取，不取前面
            for i in range(s, n):
                if t < d[i]: break
                if i > s and d[i] == d[i-1]: continue
                buffer.append(d[i])

                # 注意这里也不同，因为不可以重复取，所以i+1
                dfs(d, i+1, n, t-d[i])
                buffer.pop()

        dfs(candidates, 0, n, target)
        return res