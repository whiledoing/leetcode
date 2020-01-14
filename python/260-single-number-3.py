#/usr/bin/env python
#encoding: utf-8
'''
https://leetcode.com/problems/single-number-iii/description/

- 分两步走，第一步异或找到两个不同数值的异或总和。
- 根据异或得到具体哪一位不一样，这就**构成了二元分类的基础**
- 根据分类在异或，得到两者的数值
'''
import functools

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        diff = functools.reduce(lambda x,y: x^y, nums)

        # tricky: get least useful bit. or by using diff&(-diff)
        diff = diff - (diff&(diff-1))
        r1, r2 = 0, 0
        for num in nums:
            if num & diff:
                r1 ^= num
            else:
                r2 ^= num

        return [r1, r2]
