#/usr/bin/env python
#encoding: utf-8

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        i, n, res = 0, len(nums), []
        while i < n-2:
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue

            v, start, end = nums[i], i + 1, n - 1
            while start < end:
                vv = v + nums[start] + nums[end]
                if vv == 0:
                    res.append([v, nums[start], nums[end]])
                    start += 1
                elif vv > 0:
                    end -= 1
                else:
                    start += 1
            i += 1

        return res

if __name__ == '__main__':
    res = Solution().threeSum([-1, 0, 1, 2, -1, -4])
    print(res)