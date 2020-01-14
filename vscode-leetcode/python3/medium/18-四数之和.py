#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
# https://leetcode-cn.com/problems/4sum/description/
#
# algorithms
# Medium (36.45%)
# Likes:    357
# Dislikes: 0
# Total Accepted:    47.9K
# Total Submissions: 131.3K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c
# + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
#
# 注意：
#
# 答案中不可以包含重复的四元组。
#
# 示例：
#
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
#
# 满足要求的四元组集合为：
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
#
#
#
from typing import List

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        i, n, output = 0, len(nums), []
        while i < n:
            j, k, t = i+1, n-1, nums[i]
            while j < k:
                res = nums[j] + nums[k] + t
                if res > target: k -= 1
                elif res < target: j += 1
                else:
                    output.append((nums[i], nums[j], nums[k]))
                    while j < k and nums[j] == nums[j+1]: j += 1
                    while j < k and nums[k] == nums[k-1]: k -= 1
                    j += 1; k -= 1

            while i+1 < n and nums[i] == nums[i+1]: i += 1
            i += 1

        return output

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        i = 0
        res = []
        while i < len(nums) - 3:
            res.extend([(nums[i], *v) for v in self.threeSum(nums[i+1:], target-nums[i])])
            while i < len(nums) - 4 and nums[i] == nums[i+1]: i += 1
            i += 1
        return res

# @lc code=end
print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))

