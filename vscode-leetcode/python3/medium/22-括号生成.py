#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (72.70%)
# Likes:    677
# Dislikes: 0
# Total Accepted:    63.3K
# Total Submissions: 87.1K
# Testcase Example:  '3'
#
# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
#
#
#

from typing import List
# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(s, left, right):
            if right == 0:
                yield s

            if left:
                yield from dfs(s+'(', left-1, right)

            if right > left:
                yield from dfs(s+')', left, right-1)

        return list(dfs('', n, n))

    def generateParenthesis_using_dp(self, n: int) -> List[str]:
        dp = [['']] + [[] for _ in range(n)]
        for i in range(1, n+1):
            for j in range(i):
                dp[i] += [f"({x}){y}" for x in dp[j] for y in dp[i-1-j]]
        return dp[-1]

# @lc code=end
print(Solution().generateParenthesis(5))

