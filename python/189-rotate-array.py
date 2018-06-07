#/usr/bin/env python
#encoding: utf-8

'''
非常数学的思维，考虑将AB变为BA，用转置的概念:
$$BA = {B^TA^T}^T$$
'''
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = n - k % n
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)
        self.reverse(nums, 0, n-1)

    def reverse(self, nums, i, j):
        while i < j:
            t = nums[i]
            nums[i] = nums[j]
            nums[j] = t
            i+=1
            j-=1

def main():
    input = [1,2,3,4,5,6,7]
    Solution().rotate(input, 3)
    assert(input == [5,6,7,1,2,3,4])

if __name__ == '__main__':
    main()