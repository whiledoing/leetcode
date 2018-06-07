/**
 * Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

- 一个简单简洁的方法是从中间开始往两边搜索，使用j记做偏移量。需要注意，分为两种情况
 */
class Solution {
    public int countSubstrings(String s) {
        int res = 0, n = s.length();
        for(int i = 0; i < n; i++){
            for(int j = 0; i-j >= 0 && i+j < n && s.charAt(i-j) == s.charAt(i+j); j++)res++; //substring s[i-j, ..., i+j]
            for(int j = 0; i-1-j >= 0 && i+j < n && s.charAt(i-1-j) == s.charAt(i+j); j++)res++; //substring s[i-1-j, ..., i+j]
        }
        return res;
        /**
        int res = 0, n = s.length();
        for(int i = 0; i < n; i++) {
            for(int j = 0; i-j>=0 && i+j<n && s[i-j] == s[i+j]; j++) res++;
            for(int j = 0; i-1-j>=0 && i+j<n && s[i-1-j] == s[i+j]; j++) res++;
        }
        return res;
        **/
    }
}

private class Test {
    public static void main(String[] args) {
        new Solution().countSubstrings("abcba");
    }
}