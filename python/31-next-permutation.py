#/usr/bin/env python
#encoding: utf-8

"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

考虑清楚permutation的计算逻辑，比如：

1,3,4,2 -> 1,4,2,3

- 正看，到3的时候，发现后面已经没有可以变化了（递减），所以找到下一个数字4，放到第二位，后面的序列是第一个排列，就是从小到大。
- 所以为了找到3这个位置，从**后面开始考虑**，找到第一个不递增的，表示需要换掉，然后找到第一个需要换掉的数字，交换。
- 注意一个特点，交换后，还是有序的，而且是降序，所以reverse一下就正序了。
- 细节注意：如果nums开始就是最后一种排列，直接reverse即可。
"""


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums: return nums
        l = len(nums)
        i, j = l - 2, l - 1

        # i can change to -1, means nums in ascending order
        # get the first none ascending order
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # if so, reverse num itself
        if i == -1:
            nums.reverse()
            return

        # find the first number great then need swap number
        while j > i and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = nums[i + 1:][::-1]