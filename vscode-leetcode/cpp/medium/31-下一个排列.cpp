/*
 * @lc app=leetcode.cn id=31 lang=cpp
 *
 * [31] 下一个排列
 *
 * https://leetcode-cn.com/problems/next-permutation/description/
 *
 * algorithms
 * Medium (32.40%)
 * Likes:    344
 * Dislikes: 0
 * Total Accepted:    35.8K
 * Total Submissions: 110.5K
 * Testcase Example:  '[1,2,3]'
 *
 * 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
 *
 * 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
 *
 * 必须原地修改，只允许使用额外常数空间。
 *
 * 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
 * 1,2,3 → 1,3,2
 * 3,2,1 → 1,2,3
 * 1,1,5 → 1,5,1
 *
 */

#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
using namespace std;

// @lc code=start
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int i = nums.size() - 1;
        for (; i > 0 && nums[i-1] >= nums[i]; --i);
        if (i == 0) {
            reverse_vector(nums, 0, nums.size());
            cout << print_vector(nums) << endl;
            return;
        }

        reverse_vector(nums, i, nums.size());
        auto next_v = upper_bound(nums.begin()+i, nums.end(), nums[i-1]);
        swap(*next_v, nums[i-1]);
        cout << print_vector(nums) << endl;
    }

private:
    string print_vector(const vector<int>& v) {
        if (v.empty()) return "";
        ostringstream oss;
        copy(v.begin(), v.end(), ostream_iterator<int>(oss, ","));
        string res = oss.str();
        return res.substr(0, res.length()-1);
    }

    void reverse_vector(vector<int>& v, int begin, int end) {
        reverse(v.begin() + begin, v.begin() + end);
    }
};
// @lc code=end
int main(int argc, char const *argv[])
{
    {
        vector<int> input = {1, 1};
        Solution().nextPermutation(input);
    }
    {
        vector<int> input = {1, 2, 3};
        Solution().nextPermutation(input);
    }
    {
        vector<int> input = {1, 5, 1};
        Solution().nextPermutation(input);
    }
    {
        vector<int> input = {2, 3, 5, 1, 6, 4};
        Solution().nextPermutation(input);
    }
    return 0;
}

