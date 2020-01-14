/*
 * @lc app=leetcode.cn id=77 lang=cpp
 *
 * [77] 组合
 *
 * https://leetcode-cn.com/problems/combinations/description/
 *
 * algorithms
 * Medium (71.88%)
 * Likes:    197
 * Dislikes: 0
 * Total Accepted:    29.9K
 * Total Submissions: 41.5K
 * Testcase Example:  '4\n2'
 *
 * 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
 *
 * 示例:
 *
 * 输入: n = 4, k = 2
 * 输出:
 * [
 * ⁠ [2,4],
 * ⁠ [3,4],
 * ⁠ [2,3],
 * ⁠ [1,2],
 * ⁠ [1,3],
 * ⁠ [1,4],
 * ]
 *
 */

#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        dfs(1, n, k);
        return res;
    }

    void dfs(int start, int n, int k) {
        if (k == 0) {
            res.push_back(buffer);
            return;
        }

        for (int i = start; i <= n; ++i) {
            buffer.push_back(i);
            dfs(i+1, n, k-1);
            buffer.pop_back();
        }
    }

private:
    vector<int> buffer;
    vector<vector<int>> res;
};
// @lc code=end

