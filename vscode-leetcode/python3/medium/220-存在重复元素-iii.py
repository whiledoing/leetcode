#
# @lc app=leetcode.cn id=220 lang=python3
#
# [220] 存在重复元素 III
#
# https://leetcode-cn.com/problems/contains-duplicate-iii/description/
#
# algorithms
# Medium (25.48%)
# Likes:    115
# Dislikes: 0
# Total Accepted:    10.8K
# Total Submissions: 42.3K
# Testcase Example:  '[1,2,3,1]\n3\n0'
#
# 给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j
# 之间的差的绝对值最大为 ķ。
#
# 示例 1:
#
# 输入: nums = [1,2,3,1], k = 3, t = 0
# 输出: true
#
# 示例 2:
#
# 输入: nums = [1,0,1,1], k = 1, t = 2
# 输出: true
#
# 示例 3:
#
# 输入: nums = [1,5,9,1,5,9], k = 2, t = 3
# 输出: false
#
#

# 数据范围 t 内的数据，想到用 t 作为范围进行分桶，这样等于将之前的数据进行了映射。
# 数据范围在 t 内，等于要么一个桶，要么前后桶。
# 将数据范围 k 作为窗口大小，每次都只维护 k 范围内数据的分桶数据。注意，每个桶只有一个数据，如果有多个数据，早就成功返回了。

# 很好的题解：https://www.hrwhisper.me/leetcode-contains-duplicate-i-ii-iii/

# 另外，这里比较好的方式是使用 bst 结构，维护 k 长度的数据 set，然后找到数据的上下限。
# 比如 java 的 treeset，或者c++的 set 结构。

from typing import List

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k < 0 or t < 0:
            return False

        w = {}
        for i, v in enumerate(nums):
            index = v//(t+1)
            for m in (w.get(index), w.get(index-1), w.get(index+1)):
                if m is not None and abs(m-v) <= t:
                    return True
            w[index] = v

            if len(w) > k:
                w.pop(nums[i-k]//(t+1))

        return False


# @lc code=end

