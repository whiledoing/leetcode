/*
 * @lc app=leetcode.cn id=220 lang=cpp
 *
 * [220] 存在重复元素 III
 *
 * https://leetcode-cn.com/problems/contains-duplicate-iii/description/
 *
 * algorithms
 * Medium (25.48%)
 * Likes:    115
 * Dislikes: 0
 * Total Accepted:    10.8K
 * Total Submissions: 42.3K
 * Testcase Example:  '[1,2,3,1]\n3\n0'
 *
 * 给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j
 * 之间的差的绝对值最大为 ķ。
 *
 * 示例 1:
 *
 * 输入: nums = [1,2,3,1], k = 3, t = 0
 * 输出: true
 *
 * 示例 2:
 *
 * 输入: nums = [1,0,1,1], k = 1, t = 2
 * 输出: true
 *
 * 示例 3:
 *
 * 输入: nums = [1,5,9,1,5,9], k = 2, t = 3
 * 输出: false
 *
 */
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <initializer_list>
using namespace std;

// @lc code=start
class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        set<long> s;
        long tt = t;
        for (int i = 0; i < nums.size(); ++i) {
            int v = nums[i];

            const auto& lower = s.lower_bound(v - tt);
            if (lower != s.end() && *lower <= v + tt) {
                return true;
            }

            s.insert(v);
            if (s.size() > k) {
                s.erase(nums[i-k]);
            }
        }
        return false;
    }
};

// @lc code=end
int main(int argc, char const *argv[])
{
    {
        vector<int> v = {1, 2, 3, 1};
        cout << Solution().containsNearbyAlmostDuplicate(v, 3, 0) << endl;
    }

    {
        vector<int> v = {1,5,9,1,5,9};
        cout << Solution().containsNearbyAlmostDuplicate(v, 2, 3) << endl;
    }
}
