/*
 * @lc app=leetcode.cn id=11 lang=cpp
 *
 * [11] 盛最多水的容器
 *
 * https://leetcode-cn.com/problems/container-with-most-water/description/
 *
 * algorithms
 * Medium (60.16%)
 * Likes:    1001
 * Dislikes: 0
 * Total Accepted:    119.5K
 * Total Submissions: 198.4K
 * Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
 *
 * 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为
 * (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
 *
 * 说明：你不能倾斜容器，且 n 的值至少为 2。
 *
 *
 *
 * 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
 *
 *
 *
 * 示例:
 *
 * 输入: [1,8,6,2,5,4,8,3,7]
 * 输出: 49
 *
 */

/**
 * 这个题目有点类似「求两数之和」，都是从两边开始搜索，每次缩小一个搜索范围，直到收敛。
 *
 * 为什么可以想到从两边搜索：
 *
 * 1. 最大的面积 => 越高 * 越长
 * 2. 控制变量：先控制越长。在长固定的情况下，控制高度。
 *
 * 所以，从两边搜索，长度先是固定，在选择了一个最小的高度后，这个高度就不再有用了。后续不论另外一边如何
 * 变化，都不会超越目前「上限」，等于直接将搜索给剪枝了。
 */

#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    int maxArea(vector<int>& height) {
        int max_res = 0, i = 0, j = height.size() - 1;

        while (i < j) {
            int min_h = min(height[i], height[j]);
            max_res = max(max_res, min_h * (j-i));
            while (height[i] <= min_h && i < j) ++i;
            while (height[j] <= min_h && i < j) --j;
        }

        return max_res;
    }
};
// @lc code=end

