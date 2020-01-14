#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#
# https://leetcode-cn.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (46.06%)
# Likes:    505
# Dislikes: 0
# Total Accepted:    83.5K
# Total Submissions: 181.2K
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
#
# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
#
# L   C   I   R
# E T O E S I I G
# E   D   H   N
#
#
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
#
# 请你实现这个将字符串进行指定行数变换的函数：
#
# string convert(string s, int numRows);
#
# 示例 1:
#
# 输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"
#
#
# 示例 2:
#
# 输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
# 解释:
#
# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G
#
#

# @lc code=start
from itertools import chain, zip_longest

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1: return s
        res = []
        delta = 2*(numRows-1)
        res.extend(s[0::delta])
        for i in range(1, numRows-1):
            list_one = s[i::delta]
            list_two = s[2*(numRows-i-1)+i::delta]
            res.extend(chain(*zip_longest(list_one, list_two, fillvalue='')))

        res.extend(s[numRows-1::delta])
        return ''.join(res)


# @lc code=end
if __name__ == "__main__":
    print(Solution().convert('LEETCODEISHIRING', 4))
