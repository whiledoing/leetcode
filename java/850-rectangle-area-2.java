/**
We are given a list of (axis-aligned) rectangles.  Each rectangle[i] = [x1, y1, x2, y2] , where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the ith rectangle.

Find the total area covered by all rectangles in the plane.  Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:

Input: [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: As illustrated in the picture.
Example 2:

Input: [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 10^18 modulo (10^9 + 7), which is (10^9)^2 = (-7)^2 = 49.

- 同样的解法，python TLE，java AC。
- 本质上是O(2^n)解法，暂时没有想到更好的方法，不过可以AC，说明是可行解。
- 计算重叠面积转为一个递归问题，dfs(A) = area(A[0]) + dfs(A[1:]) - dfs(A[0] intersection A[1:])
- 一个计算的优化方法是将空集从dfs中删除，这样子可以比较快速的消除intersection集合的大小，提高速度。
*/

public class Solution {
    public static void main(String[] args) {
//        int[][] input = new int[3][];
//        input[0] = new int[] {0,0,2,2};
//        input[1] = new int[] {1,0,2,3};
//        input[2] = new int[] {1,0,3,1};

        int[][] input = new int[1][];
        input[0] = new int[] {0,0,1000000000,1000000000};
        System.out.println(new Test().rectangleArea(input));
    }

    public int rectangleArea(int[][] rectangles) {
        return dfs(Arrays.asList(rectangles));
    }

    public long area(int[] rec) {
        long w = rec[2] - rec[0];
        long h = rec[3] - rec[1];
        return w > 0 && h > 0 ? w*h : 0;
    }

    public int[] inter_sect(int[] a, int[] b) {
        int c1 = Math.max(a[0], b[0]);
        int c2 = Math.max(a[1], b[1]);
        int d1 = Math.min(a[2], b[2]);
        int d2 = Math.min(a[3], b[3]);
        return c1 >= d1 || c2 >= d2 ? null : new int[] {c1, c2, d1, d2};
    }

    public int dfs(List<int []> A) {
        if(A.size() == 0) return 0;

        // 只保存有效的交集，降低dfs的维度
        int[] first = A.get(0);
        List<int[]> new_A = new ArrayList<>();
        for (int i = 1; i < A.size(); i++) {
            int[] new_v = inter_sect(first, A.get(i));
            if(new_v != null) {
                new_A.add(new_v);
            }
        }

        long res = area(first) + dfs(A.subList(1, A.size())) - dfs(new_A);
        return (int)(res % (int)(Math.pow(10, 9) + 7));
    }
}