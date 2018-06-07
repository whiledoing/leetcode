#!/usr/bin/env python
#encoding: utf-8

'''
In a 2D grid from (0, 0) to (N-1, N-1), every cell contains a 1, except those cells in the given list mines which are 0. What is the largest axis-aligned plus sign of 1s contained in the grid? Return the order of the plus sign. If there is none, return 0.

An "axis-aligned plus sign of 1s of order k" has some center grid[x][y] = 1 along with 4 arms of length k-1 going up, down, left, and right, and made of 1s. This is demonstrated in the diagrams below. Note that there could be 0s or 1s beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1s.

Examples of Axis-Aligned Plus Signs of Order k:

Order 1:
000
010
000

Order 2:
00000
00100
01110
00100
00000

Order 3:
0000000
0001000
0001000
0111110
0001000
0001000
0000000
Example 1:

Input: N = 5, mines = [[4, 2]]
Output: 2
Explanation:
11111
11111
11111
11111
11011
In the above grid, the largest plus sign can only be order 2.  One of them is marked in bold.
Example 2:

Input: N = 2, mines = []
Output: 1
Explanation:
There is no plus sign of order 2, but there is of order 1.
Example 3:

Input: N = 1, mines = [[0, 0]]
Output: 0
Explanation:
There is no plus sign, so return 0.
Note:

N will be an integer in the range [1, 500].
mines will have length at most 5000.
mines[i] will be length 2 and consist of integers in the range [0, N-1].
(Additionally, programs submitted in C, C++, or C# will be judged with a slightly smaller time limit.)
'''

class Solution:
    # 最开始的方案
    # 其实应该进行4次DP，从4个方向分别计算连续1的个数
    # 这里每次进行两个方向，利用了DP的连续性
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        import sys
        dp_1 = [[(0, 0)]*(N+2) for _ in range(N+2)]
        res = 0

        # 同时对左和上两个方向进行DP
        mines_m = {(x, y):True for x, y in mines}
        for i in range(N):
            for j in range(N):
                if (i,j) not in mines_m:
                    dp_1[i+1][j+1] = (dp_1[i+1][j][0]+1, dp_1[i][j+1][1]+1)

        # 同时对右和下两个方向进行DP，同时计算4个方向的最小值，同时统计结果最大值
        for i in range(N-1, -1, -1):
            for j in range(r-1, -1, -1):
                if (i,j) not in mines_m:
                    new_v = dp_1[i+1][j+2][0]+1, dp_1[i+2][j+1][1]+1
                    res = max(res, min(dp_1[i+1][j+1][0], dp_1[i+1][j+1][0][1], new_v[0], new_v[1]))
                    dp_1[i+1][j+1] = new_v

        return res

        # 参考了答案：https://leetcode.com/problems/largest-plus-sign/discuss/113314/JavaC++Python-O(N2)-solution-using-only-one-grid-matrix
        # 本质上一样，从4个方向计算，但是这里并不需要**DP来保存状态**，从左到右遍历，只需要知道左边（前一个）的结果即可，所以这里使用l,r,u,d分别表示
        # 这样子完全可以用一个结构grid来保存每个节点的最小值。
        # 实现的tricky在于，使用i，j，k来表示4个方向的遍历
        def orderOfLargestPlusSign_good_one(self, N, mines):
            """
            :type N: int
            :type mines: List[List[int]]
            :rtype: int
            """
            grid = [[N] * N for i in range(N)]

            for m in mines:
                grid[m[0]][m[1]] = 0

            for i in range(N):
                l, r, u, d = 0, 0, 0, 0

                for j, k in zip(range(N), reversed(range(N))):
                    # i从上到下，j，k表示列坐标，分别从左到右，和从右到左
                    l = l + 1 if grid[i][j] != 0 else 0
                    grid[i][j] = min(grid[i][j], l)

                    r = r + 1 if grid[i][k] != 0 else 0
                    grid[i][k] = min(grid[i][k], r)

                    # i表示从左到右，j，k表示行坐标，分别从上到小，和从下到上
                    u = u + 1 if grid[j][i] != 0 else 0
                    grid[j][i] = min(grid[j][i], u)

                    d = d + 1 if grid[k][i] != 0 else 0
                    grid[k][i] = min(grid[k][i], d)

            return max([max(row) for row in grid])
