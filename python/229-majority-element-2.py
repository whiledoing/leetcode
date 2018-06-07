#/usr/bin/env python
#encoding: utf-8
'''
实现的非常nb，具体参考https://leetcode.com/problems/majority-element-ii/discuss/63520/Boyer-Moore-Majority-Vote-algorithm-and-my-elaboration

- 如果找到floor(n/3)的元素，可以想到最多就2个
- 使用Boyer-Moore的方法找到主元素
- 使用两个candidate计数，如果找到就累加，如果不是就减一，如果没有计数，就标记candidate
- 实现的时候先判断是否和candidate相同，这样子可以保证cd_1和cd_2不会重复。
'''
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c_1, c_2, cd_1, cd_2 = 0,0,-1,-2
        for v in nums:
            if cd_1 == v:
                c_1 += 1
            elif cd_2 == v:
                c_2 += 1
            elif c_1 == 0:
                c_1, cd_1 = 1, v
            elif c_2 == 0:
                c_2, cd_2 = 1, v
            else:
                c_1, c_2 = c_1-1, c_2-1

        return [c for c in [cd_1, cd_2] if nums.count(c) > len(nums) // 3]

def main():
    res = Solution().majorityElement([1,1,1,3,3,2,2,2])
    assert(res == [1,2])

if __name__ == '__main__':
    main()