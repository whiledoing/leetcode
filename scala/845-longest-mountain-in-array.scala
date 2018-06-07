/*
845. Longest Mountain in Array My SubmissionsBack to Contest
User Accepted: 1154
User Tried: 1384
Total Accepted: 1170
Total Submissions: 4306
Difficulty: Medium
Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain.

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.

Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000

- 连续的上升问题，只和前一个数据的状态有关，考虑用dp记录连续上升的个数。
- dp计算时，考虑将统计最值变为统计**连续上升**的个数，这样子便于直接计算长度。
- 问题分解：高峰 => 两个维度的最长上升个数。想到从左到右，和从右到左进行扫描的套路。
*/
object Solution {
    def longestMountain(A: Array[Int]): Int = {
        val n = A.length
        val up = new Array[Int](n)
        val down = new Array[Int](n)
        var i = 0
        var res = 0

        // 从左到右分析递增的数据个数
        for (i <- 1 until n) {
            if (A(i) > A(i - 1)) up(i) = up(i - 1) + 1
        }

        // 从右到左分析递增的数据个数，高峰就是两边都有下降的节点，同时加上自己本身
        for (i <- n - 2 to 0 by -1) {
            if (A(i) > A(i + 1)) down(i) = down(i + 1) + 1

            // 注意，这里需要判断是否是高峰，如果不是，不可以统计
            if(up(i) > 0 && down(i) > 0) res = math.max(res, up(i) + down(i) + 1)
        }

        return res
    }
}