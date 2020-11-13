#
# @lc app=leetcode.cn id=402 lang=python3
#
# [402] 移掉K位数字
#
# https://leetcode-cn.com/problems/remove-k-digits/description/
#
# algorithms
# Medium (27.24%)
# Likes:    138
# Dislikes: 0
# Total Accepted:    9.3K
# Total Submissions: 34.1K
# Testcase Example:  '"1432219"\n3'
#
# 给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。
#
# 注意:
#
#
# num 的长度小于 10002 且 ≥ k。
# num 不会包含任何前导零。
#
#
# 示例 1 :
#
#
# 输入: num = "1432219", k = 3
# 输出: "1219"
# 解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。
#
#
# 示例 2 :
#
#
# 输入: num = "10200", k = 1
# 输出: "200"
# 解释: 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
#
#
# 示例 3 :
#
#
# 输入: num = "10", k = 2
# 输出: "0"
# 解释: 从原数字移除所有的数字，剩余为空就是0。
#
#
#

# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        k = len(num) - k
        if k <= 0: return '0'

        self.res = 'a'
        def dfs(s, buffer):
            # print(buffer)
            if len(buffer) == k:
                self.res = min(self.res, buffer)
                return

            if len(num) - s + len(buffer) < k:
                return

            for i in range(s, len(num)):
                if i > 0 and (num[i] == num[i-1]): continue
                dfs(i+1, buffer + num[i])

        dfs(0, '')
        return self.res

# @lc code=end
print(Solution().removeKdigits("10200", 1))

