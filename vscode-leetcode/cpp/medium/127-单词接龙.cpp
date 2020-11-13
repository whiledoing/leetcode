/*
 * @lc app=leetcode.cn id=127 lang=cpp
 *
 * [127] 单词接龙
 *
 * https://leetcode-cn.com/problems/word-ladder/description/
 *
 * algorithms
 * Medium (45.33%)
 * Likes:    632
 * Dislikes: 0
 * Total Accepted:    85.2K
 * Total Submissions: 188K
 * Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
 *
 * 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord
 * 的最短转换序列的长度。转换需遵循如下规则：
 *
 *
 * 每次转换只能改变一个字母。
 * 转换过程中的中间单词必须是字典中的单词。
 *
 *
 * 说明:
 *
 *
 * 如果不存在这样的转换序列，返回 0。
 * 所有单词具有相同的长度。
 * 所有单词只由小写字母组成。
 * 字典中不存在重复的单词。
 * 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
 *
 *
 * 示例 1:
 *
 * 输入:
 * beginWord = "hit",
 * endWord = "cog",
 * wordList = ["hot","dot","dog","lot","log","cog"]
 *
 * 输出: 5
 *
 * 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
 * ⁠    返回它的长度 5。
 *
 *
 * 示例 2:
 *
 * 输入:
 * beginWord = "hit"
 * endWord = "cog"
 * wordList = ["hot","dot","dog","lot","log"]
 *
 * 输出: 0
 *
 * 解释: endWord "cog" 不在字典中，所以无法进行转换。
 *
 */
#include <algorithm>
#include <queue>
#include <string>
#include <unordered_set>
#include <vector>
using namespace std;

// @lc code=start
class Solution {
 public:
  int ladderLength(string beginWord, string endWord, vector<string> &wordList) {
    unordered_set<string> left_map(wordList.begin(), wordList.end());
    queue<string> q;
    q.push(beginWord);
    left_map.erase(beginWord);

    int ladder = 2;
    while (!q.empty()) {
      int s = q.size();
      for (size_t i = 0; i < s; i++) {
        string search_word = q.front();
        q.pop();

        for (size_t i = 0; i < search_word.size(); ++i) {
          char c = search_word[i];
          for (size_t j = 0; j < 26; j++) {
            search_word[i] = 'a' + j;
            if (left_map.find(search_word) != left_map.end()) {
              if (search_word == endWord) {
                return ladder;
              }

              q.push(search_word);
              left_map.erase(search_word);
            }
          }
          search_word[i] = c;
        }
      }
      ++ladder;
    }
    return 0;
  }
};
// @lc code=end

int main(int argc, char const *argv[]) {
  vector<string> input{"hot", "dot", "dog", "lot", "log"};
  Solution().ladderLength("hit", "cog", input);
  return 0;
}
