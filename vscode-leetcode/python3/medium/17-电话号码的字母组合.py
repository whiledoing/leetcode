#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (51.82%)
# Likes:    530
# Dislikes: 0
# Total Accepted:    66.9K
# Total Submissions: 129.2K
# Testcase Example:  '"23"'
#
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
#
#
# 示例:
#
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
#
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
#
#

from typing import List
# @lc code=start
class Solution:
    mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

    def letterCombinations(self, digits: str) -> List[str]:
        return (
            [] if len(digits) == 0 else
            list(Solution.mapping[digits[0]]) if len(digits) == 1
            else [c+left for c in Solution.mapping[digits[0]] for left in self.letterCombinations(digits[1:])]
        )

    def letterCombinations_version_1(self, digits: str) -> List[str]:
        if not digits: return []
        dfs = lambda d: [c + left for c in Solution.mapping[d[0]] for left in dfs(d[1:])] if d else ['']
        return dfs(digits)


# @lc code=end
print(Solution().letterCombinations("23"))

