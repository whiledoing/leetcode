/*
 * @lc app=leetcode.cn id=240 lang=cpp
 *
 * [240] 搜索二维矩阵 II
 *
 * https://leetcode-cn.com/problems/search-a-2d-matrix-ii/description/
 *
 * algorithms
 * Medium (42.39%)
 * Likes:    473
 * Dislikes: 0
 * Total Accepted:    87.2K
 * Total Submissions: 205.5K
 * Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n' +
  '5'
 *
 * 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：
 *
 *
 * 每行的元素从左到右升序排列。
 * 每列的元素从上到下升序排列。
 *
 *
 * 示例:
 *
 * 现有矩阵 matrix 如下：
 *
 * [
 * ⁠ [1,   4,  7, 11, 15],
 * ⁠ [2,   5,  8, 12, 19],
 * ⁠ [3,   6,  9, 16, 22],
 * ⁠ [10, 13, 14, 17, 24],
 * ⁠ [18, 21, 23, 26, 30]
 * ]
 *
 *
 * 给定 target = 5，返回 true。
 *
 * 给定 target = 20，返回 falsej
 *
 */

/*
https://leetcode-cn.com/problems/search-a-2d-matrix-ii/solution/sou-suo-er-wei-ju-zhen-ii-by-leetcode-2/

这个题目比较有趣的点在于：

- 找到一个二元决策点，每次搜索，都可以有效进行二元抉择
- 这样，在每次抉择后，所有的选择空间缩小一倍。
- 这里必须选择「右下或者左上」，每次判定数据，都会缩小一行或者一列。向左或者向右，一边是更大，一边是更小。
*/

#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

// @lc code=start
class Solution {
 public:
  bool searchMatrix(vector<vector<int>>& matrix, int target) {
    if (matrix.size() == 0) return false;
    int row = matrix.size() - 1, col = 0;
    int width = matrix[0].size();

    while (row >= 0 && col < width) {
      if (matrix[row][col] > target)
        --row;
      else if (matrix[row][col] < target)
        ++col;
      else
        return true;
    }

    return false;
  }
};
// @lc code=end

int main(int argc, char const* argv[]) {
  vector<vector<int>> test;
  Solution().searchMatrix(test, 0);
  return 0;
}
