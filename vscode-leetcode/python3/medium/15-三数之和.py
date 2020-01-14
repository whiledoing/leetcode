#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (24.88%)
# Likes:    1664
# Dislikes: 0
# Total Accepted:    137.5K
# Total Submissions: 551.8K
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
#
#
#

from typing import List

# @lc code=start
class Solution:
    def threeSum_using_set(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i, n, output = 0, len(nums), set()
        while i < n:
            j, k, t = i+1, n-1, nums[i]
            while j < k:
                res = nums[j] + nums[k] + t
                if res > 0: k -= 1
                elif res < 0: j += 1
                else:
                    output.add((nums[i], nums[j], nums[k]))
                    j += 1; k -= 1
            i += 1

        return list(output)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i, n, output = 0, len(nums), []
        while i < n:
            j, k, t = i+1, n-1, nums[i]
            while j < k:
                res = nums[j] + nums[k] + t
                if res > 0: k -= 1
                elif res < 0: j += 1
                else:
                    output.append((nums[i], nums[j], nums[k]))
                    while j < k and nums[j] == nums[j+1]: j += 1
                    while j < k and nums[k] == nums[k-1]: k -= 1
                    j += 1; k -= 1

            while i+1 < n and nums[i] == nums[i+1]: i += 1
            i += 1

        return output
# @lc code=end
print(Solution().threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))

