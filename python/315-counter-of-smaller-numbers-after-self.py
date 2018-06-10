#/usr/bin/env python
#encoding: utf-8

"""
Input: [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

- 想到merge sort过程中反序过程
- 这里不同于merge sort在于是对**原始数据的序号进行排序**，这样子才可以在merge的时候知道哪一个数据反序了多少次。

- 最气人的来了，看了答案最快速的答案居然直接是二分查找，虽然insert的过程是O(n)，涉及到元素移动，但大多数的这个时间
- 可能非常的快，毕竟insert，insort_left这些操作可能是C的代码实现，所以非常高效。而脚本层的实现即时算法高级，但也抵不过底层的优化。手动哭笑不得。
"""

class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        buffer, res = [0] * n, [0] * n

        # 注意是对ind进行排序
        ind = list(range(0, n))

        def merge_sort(l, r):
            if l >= r: return
            m = l + ((r - l) >> 1)
            merge_sort(l, m)
            merge_sort(m + 1, r)

            i, j, k = l, m + 1, 0
            while i <= m:
                while j <= r and nums[ind[i]] > nums[ind[j]]:
                    buffer[k], k, j = ind[j], k + 1, j + 1

                # 这样子说明ind[i]这个元素被后面的元素反序了
                res[ind[i]] += j - m - 1
                buffer[k], k, i = ind[i], k + 1, i + 1

            # while j <= r:
            #     buffer[k], k, j = ind[j], k + 1, j + 1
            # ind[l:r + 1] = buffer[:k]

            # 更高效，因为后面的不需要计算
            ind[l:l+k] = buffer[:k]

        merge_sort(0, n - 1)
        return res

    def countSmaller_with_binary_search(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import bisect
        n = len(nums)
        buff, res = [], [0] * n
        for i in range(n - 1, -1, -1):
            res[i] = bisect.bisect_left(buff, nums[i])

            # 112ms
            buff.insert(res[i], nums[i])

            # 120ms
            # bisect.insort_left(buff, nums[i])
        return res