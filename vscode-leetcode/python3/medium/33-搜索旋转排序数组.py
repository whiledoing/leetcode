#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (36.23%)
# Likes:    458
# Dislikes: 0
# Total Accepted:    63.9K
# Total Submissions: 176.3K
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
# 你可以假设数组中不存在重复的元素。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 示例 1:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
#
#
# 示例 2:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1
#
#

from typing import List
import bisect

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        self.nums, self.target = nums, target
        # 这里非常巧妙，不用自己手写二分搜索。利用系统的 bisect
        # 以为 getitem 返回的数值表示是否到左边搜索，所以第一个 True 的值就是收敛的位置。
        # bisetct的输入是【array, value, left_index, right_index】
        i = bisect.bisect_left(self, True, 0, len(nums))

        # 二分找到的是第一个大于等于当前值的位置，用来 insert 插入。所以还需要判断一下是否是搜索的数值
        # 类似于C++中的 binary_search 之于 lower_bound 的检测。
        # 另外需要注意，可能insert 的位置是最后一位，所以需要检测 i 的范围
        return i if i < len(nums) and nums[i] == target else -1

    def __getitem__(self, i):
        s, m, t = self.nums[0], self.nums[i], self.target
        # 二分进行的搜索条件，如果 target 在 s 和 m 之间，单调递增，说明 s 和 m 有序，返回 True，表示需要左移动搜索
        # 如果 s 和 m 之前不是单调递增，说明之间有旋转导致的 gap：t 比 m 还小或者 t 比 s 还大，说明搜索还在左边范围内。（右边的范围是[m, s]）
        return (s <= t <= m) or (t <= m < s) or (m < s <= t)

# @lc code=end
if __name__ == "__main__":
    print(Solution().search([3, 1], 1))
    print(Solution().search([4,5,6,7,0,1,2], 0))
    print(Solution().search([4,5,6,7,0,1,2], 3))
