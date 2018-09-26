#/usr/bin/env python3
#encoding: utf-8

"""
You have 4 cards each containing a number from 1 to 9. You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.

Example 1:
Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24
Example 2:
Input: [1, 2, 1, 2]
Output: False
Note:
The division operator / represents real division, not integer division. For example, 4 / (1 - 2/3) = 12.
Every operation done is between two numbers. In particular, we cannot use - as a unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
You cannot concatenate numbers together. For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.

分析清楚递归的方式：

- 取得数据C_n^2的combination，对任意两个排列进行相关运算，然后组合剩下的元素构成新集合，重新计算n-1个元素是否可以得到24
- 计算时注意除法导致的精度问题，当然可以用Fraction，但是时间代价高，check时使用`math.isclose`和24进行比较
- 一个实现技巧，如果b为0，可以写成`b and a/b`，因为a*b已经为0，所以多加入一个0也ok，如果不为0，刚好为a/b
"""
import math
import itertools

class Solution:
    def judgePoint24(self, nums):
        # 因为元素个数可控，手码了一下排列组合信息，提高速度
        combination_index = {
            4: [(0, 1, (2, 3)), (0, 2, (1, 3)), (0, 3, (1, 2)), (1, 2, (0, 3)), (1, 3, (0, 2)), (2, 3, (0, 1))],
            3: [(0, 1, (2,)), (0, 2, (1,)), (1, 2, (0,))],
            2: [(0, 1, ())]
        }

        res = set()
        def dfs(nums, ops):
            if len(nums) == 1:
                if math.isclose(nums[0], 24):
                    res.add(' '.join(ops))
                return

            for i, j, left_index_list in combination_index[len(nums)]:
                a, b, left = nums[i], nums[j], [nums[index] for index in left_index_list]

                # 注意实现技巧, b and a/b
                for new_num, op in itertools.zip_longest([a+b, a-b, a*b, b and a/b], ['+', '-', '*', '/']):
                    left.append(new_num)
                    ops.append('%s%s%s' % (a, op, b))
                    dfs(left, ops)
                    left.pop()
                    ops.pop()

                for new_num, op in itertools.zip_longest([b-a, a and b/a], ['-', '/']):
                    left.append(new_num)
                    ops.append('%s%s%s' % (b, op, a))
                    dfs(left, ops)
                    left.pop()
                    left.pop()
                    ops.pop()

            return False

        dfs(nums, [])
        return res

    def judgePoint24_concise_version(self, nums):
        """
        这个版本参考：https://leetcode.com/problems/24-game/discuss/107675/Short-Python

        其实是用permutation写成了生成器模式，使用any让代码更简洁。

        不过相比于combination，计算量多一些（a+b和b+a，a*b和b*a重复），不过可忽略不计（并不改变时间复杂度）
        """
        # if len(nums) == 1: return math.isclose(nums[0], 24)
        if len(nums) == 1:
            return nums[0] == 24

        return any(self.judgePoint24([x] + rest)
                    for a, b, *rest in itertools.permutations(nums)
                    for x in {a + b, a - b, a * b, b and a / b})


if __name__ == '__main__':
    print(Solution().judgePoint24([3, 7, 7, 3]))
