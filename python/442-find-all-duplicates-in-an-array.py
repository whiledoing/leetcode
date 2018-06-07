#/usr/bin/env python
#encoding: utf-8

'''
https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

- 原题说明数组中数值范围是[1, n]，其实就是提示使用数组本身来做hash。
- 数据最多出现两次，提示想到**根据负负得正**的想法来操作hash数据。
- 所以，这里将已经存在的数据变为负数（一种hash手段，有不改变原数组数值），如果两次变为负数，变成正数，说明出现了两次。
'''

class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for v in nums:
            if nums[abs(v)-1] < 0:
                res.append(abs(v))
            else:
                nums[abs(v)-1] *= -1
        return res


def main():
    res = Solution().findDuplicates([4,3,2,7,8,2,3,1])
    assert(res == [2,3])

if __name__ == '__main__':
    main()