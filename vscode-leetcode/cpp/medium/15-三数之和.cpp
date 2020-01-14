/*
 * @lc app=leetcode.cn id=15 lang=cpp
 *
 * [15] 三数之和
 *
 * https://leetcode-cn.com/problems/3sum/description/
 *
 * algorithms
 * Medium (24.88%)
 * Likes:    1664
 * Dislikes: 0
 * Total Accepted:    137.5K
 * Total Submissions: 551.8K
 * Testcase Example:  '[-1,0,1,2,-1,-4]'
 *
 * 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
 * ？找出所有满足条件且不重复的三元组。
 *
 * 注意：答案中不可以包含重复的三元组。
 *
 * 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
 *
 * 满足要求的三元组集合为：
 * [
 * ⁠ [-1, 0, 1],
 * ⁠ [-1, -1, 2]
 * ]
 *
 *
 */

#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

// @lc code=start
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> output;
        for(int i = 0; i < nums.size(); ++i) {
            int j = i+1, k = nums.size() - 1, t = nums[i];
            while (j < k) {
                int res = nums[j]+nums[k]+t;
                if (res > 0) --k;
                else if (res < 0) ++j;
                else {
                    output.push_back({nums[i], nums[j], nums[k]});
                    while (j < k && nums[j] == nums[j+1]) ++j;
                    while (j < k && nums[k] == nums[k-1]) --k;
                    ++j; --k;
                }
            }
            while (i < nums.size()-1 && nums[i] == nums[i+1]) ++i;
        }

        return output;
    }
};
// @lc code=end
int main(int argc, char const *argv[])
{
    vector<int> input = {-1, 0, 1, 2, -1, -4};
    auto&& res = Solution().threeSum(input);
    for (auto& row : res) {
        for (auto& v : row) cout << v << ' ';
        cout << endl;
    }
    return 0;
}


