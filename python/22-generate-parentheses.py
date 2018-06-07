#/usr/bin/env python
#encoding: utf-8

"""

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
]


DP解放的说明：

To generate all n-pair parentheses, we can do the following:

    Generate one pair: ()

    Generate 0 pair inside, n - 1 afterward: () (...)...

    Generate 1 pair inside, n - 2 afterward: (()) (...)...

    ...

    Generate n - 1 pair inside, 0 afterward: ((...))

I bet you see the overlapping sub-problems here. Here is the code:

(you could see in the code that x represents one j-pair solution and y represents one (i - j - 1) pair solution, and we are taking into account all possible of combinations of them)

这点非常有意思，组合问题都可以考虑用DP来求解。计算N问题，考虑是否可以用已经计算的规模来表示。
"""

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res, buffer = [], []

        # 每次对左边括号和右边括号进行统计，如果可以放左边就放左边
        # 如果可以放右边，需要看是否有左边括号可以匹配
        def dfs(l_n, r_n, n_for_r):
            if not l_n and not r_n:
                res.append(''.join(buffer))
                return

            if l_n > 0:
                buffer.append('(')
                dfs(l_n - 1, r_n, n_for_r + 1)
                buffer.pop()

            if r_n > 0 and n_for_r > 0:
                buffer.append(')')
                dfs(l_n, r_n - 1, n_for_r - 1)
                buffer.pop()

        dfs(n, n, 0)
        return res

    def generateParenthesis_with_dp(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for _ in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]


