#/usr/bin/env python
#encoding: utf-8

'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:

Input: [2,1,5,6,2,3]
Output: 10

这个题目非常的tricky，而且很绕脑袋，不过想明白之后有觉得非常神奇：

- 考虑暴力搜索的方式，每次对一个数值两边进行搜索，如果左边遇到比自己小的停止，右边遇到比自己小的停止。
- 如果顺序访问，一旦右边发现比自己小，那么可以直接停止，问题左边如何计算比自己小的数据呢？ 想到遍历时候用栈保存信息（因为向左回溯）
- 如何用栈？栈需要反应当前节点最左边符合要求的停止位置。
- 栈顶元素递增，如果当前元素大于栈顶，将元素取出，计算面积。长度为当前位置和栈顶的位置差值。栈顶表示当前元素可以向左到的边界。
- 多了一个尾元素，值为0，表示将所有的栈顶都pop出来。
'''
class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        i, s, n, max_area = 0, [], len(heights), 0
        while i <= n:
            v = heights[i] if i < n else 0

            # 无数据，或者当前数据比栈顶更
            if not s or v >= heights[s[-1]]:
                s.append(i)
                i += 1
            else:
                area_index = s.pop()
                area = heights[area_index] * (i - s[-1] - 1 if s else i)
                max_area = max(max_area, area)

        return max_area

    def largestRectangleArea_tricky_impl(self, heights):
        # 非常tricky的实现，使用了两个sentinel
        # 第一个sentinel使用heights的最后一个元素记做0，表示运行到最后进行统一的规约
        # 第二个sentinel在栈中放入-1，这样子栈中一定有元素，因为-1对应位置的数值刚好是0，用于也没有元素比0还小，所以不会出栈
        # 同时，-1也非常好的表示了边界值！！！，非常神奇和高效的实现。
        heights.append(0)
        max_v, s, n = 0, [-1], len(heights)
        for i, v in enumerate(heights):
            while v < heights[s[-1]]:
                h = heights[s.pop()]
                w = i-1-s[-1]
                max_v = max(max_v, h*w)
            s.append(i)
        return max_v