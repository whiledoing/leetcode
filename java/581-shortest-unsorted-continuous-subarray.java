/**
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
**/

/**
这个题目非常厉害。代码非常简单，但分析起来却着实耗脑子。https://leetcode.com/problems/shortest-unsorted-continuous-subarray/discuss/103066/Ideas-behind-the-O(n)-two-pass-and-one-pass-solutions

- 一个数组不是有序状态，等价于数组中某一个元素不在排序后的位置上
- 有两个解读维度：1）某个数据的左侧有比其大的数据 2）某个数据的右侧存在比其小的数据
- loop从左到右扫描最大值，从右到左扫描最小值。
- 如果某一个数值和最大，最小不同，说明左侧或者右侧存在更大或更小的元素，也就定位了第一个存在问题的位置
**/
class Solution {
    public int findUnsortedSubarray(int[] nums) {
        int i = 0, j = -1, min_v = Integer.MAX_VALUE, max_v = Integer.MIN_VALUE;
        for(int l = 0, r = nums.length-1; r >= 0; ++l, --r) {
            max_v = Math.max(max_v, nums[l]);
            if(max_v != nums[l]) j = l;

            min_v = Math.min(min_v, nums[r]);
            if(min_v != nums[r]) i = r;
        }

        return j-i+1;
    }
}