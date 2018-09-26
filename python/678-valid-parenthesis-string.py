#/usr/bin/env python
#encoding: utf-8

"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].

我自己实现的版本基于dfs的方法，因为星号可以变化为3种情况，所以dfs解析。标准答案非常nice。

- 本质上，如果没有星号，不需要stack记录括号信息，只需要一个counter，统计当前没有匹配的左括号数量即可。
- 加入了星号，有3中选择，每种选择导致counter+1或者counter-1或者不变，可以抽象为改变了counter的**范围**
- 最后检测的是，如果max range小于0，说明完全无法匹配。如果min range为0，说明可以变成匹配状态。非常nice的抽象！
"""
class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def dfs(s, stack_left, left, right, star):
            if not s: return not stack_left

            # 统计各个符号个数是为了有效剪枝，如果star无法将left和right匹配，那么直接发挥无效
            if left + star < right or right + star < left:
                return False

            for i, c in enumerate(s):
                if c == '(':
                    stack_left += 1
                elif c == ')':
                    if not stack_left: return False
                    stack_left, left, right = stack_left - 1, left - 1, right - 1
                else:
                    if dfs(s[i + 1:], stack_left, left, right, star - 1): return True
                    if dfs(s[i + 1:], stack_left + 1, left + 1, right, star - 1): return True
                    if not stack_left: return False
                    return dfs(s[i + 1:], stack_left - 1, left - 1, right, star - 1)

            return not left

        from collections import Counter
        c = Counter(s)
        return dfs(s, 0, c['('], c[')'], c['*'])

    def checkValidString_good(self, s):
        """
        代码来自于：https://leetcode.com/problems/valid-parenthesis-string/discuss/107570/Python-easy-understand-solution

        The number of open parenthesis is in a range [cmin, cmax]

        - cmax counts the maximum open parenthesis, which means the maximum number of unbalanced '(' that COULD be paired.
        - cmin counts the minimum open parenthesis, which means the number of unbalanced '(' that MUST be paired.

        The string is valid for 2 condition:

        - cmax will never be negative.
        - cmin is 0 at the end.
        """
        cmin = cmax = 0
        for i in s:
            if i == '(':
                cmax += 1
                cmin += 1
            if i == ')':
                cmax -= 1
                cmin = max(cmin - 1, 0)
            if i == '*':
                cmax += 1
                cmin = max(cmin - 1, 0)
            if cmax < 0:
                return False
        return cmin == 0
