/*
 * @lc app=leetcode.cn id=3 lang=cpp
 *
 * [3] 无重复字符的最长子串
 *
 * https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
 *
 * algorithms
 * Medium (32.33%)
 * Likes:    2935
 * Dislikes: 0
 * Total Accepted:    307.1K
 * Total Submissions: 949.9K
 * Testcase Example:  '"abcabcbb"'
 *
 * 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
 *
 * 示例 1:
 *
 * 输入: "abcabcbb"
 * 输出: 3
 * 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
 *
 *
 * 示例 2:
 *
 * 输入: "bbbbb"
 * 输出: 1
 * 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
 *
 *
 * 示例 3:
 *
 * 输入: "pwwkew"
 * 输出: 3
 * 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
 * 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
 *
 *
 */

#include <iostream>
#include <unordered_map>
using namespace std;

// @lc code=start
class Solution {
 public:
  int lengthOfLongestSubstring(string s) {
    unordered_map<char, int> m;
    int max_len = 0;
    int left = 0, right = 0;
    for (; right < s.size(); ++right) {
      auto last_index = m.find(s[right]);
      // cout << "right : " << right << " : " << (m.count(s[right]) > 0 ? m[s[right]] : -1) << endl;
      if (last_index != m.end() && last_index->second >= left) {
        max_len = max(right - left, max_len);
        // cout << "found: " << max_len << " : " << right << " : " << left << endl;
        left = last_index->second + 1;
      }
      m[s[right]] = right;
    }
    // cout << "left: " << left << endl;
    // cout << "right: " << right << endl;
    return max(max_len, right - left);
  }
};
// @lc code=end

int main(int argc, char const *argv[]) {
  cout << Solution().lengthOfLongestSubstring("abcabcbb") << endl;
  return 0;
}
