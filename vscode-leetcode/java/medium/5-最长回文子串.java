/*
 * @lc app=leetcode.cn id=5 lang=java
 *
 * [5] 最长回文子串
 *
 * https://leetcode-cn.com/problems/longest-palindromic-substring/description/
 *
 * algorithms
 * Medium (27.93%)
 * Likes:    1585
 * Dislikes: 0
 * Total Accepted:    159.1K
 * Total Submissions: 569.3K
 * Testcase Example:  '"babad"'
 *
 * 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
 *
 * 示例 1：
 *
 * 输入: "babad"
 * 输出: "bab"
 * 注意: "aba" 也是一个有效答案。
 *
 *
 * 示例 2：
 *
 * 输入: "cbbd"
 * 输出: "bb"
 *
 *
 */

// @lc code=start
class Solution {
    public String longestPalindrome(String s) {
        int i = 0;
        int maxSize = 0;
        int maxStart = 0;
        while (i < s.length()) {
            int start = i-1;
            while (i+1 < s.length() && s.charAt(i+1) == s.charAt(i)) ++i;
            int end = ++i;
            while (start >= 0 && end < s.length() && s.charAt(start) == s.charAt(end)) {
                --start;
                ++end;
            }
            start = start+1;
            if (end - start > maxSize) {
                maxSize = end - start;
                maxStart = start;
            }
        }

        return s.substring(maxStart, maxStart+maxSize);
    }

    public static void main(String[] args) {
        System.out.println(new Solution().longestPalindrome("babad"));
    }
}
// @lc code=end

