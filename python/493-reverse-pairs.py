#/usr/bin/env python
#encoding: utf-8

"""
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.

- 这里实现了集中算法：1）基于BST的搜索 2）基于BIT的统计 3）基于merge_sort
- 数组的题目就多想想：
    - 是否有子结构，有的话用dp或者dfs(with memo)
    - 是否可以进行二元划分，比如这里，分解和「左，右，合并」
    - BIT数据结构非常神奇，对于范围统计很有效。
"""

def reversePairs_first_version_not_work(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 本来考虑的方法是对值域进行统计（2^32-1）的数据进行桶排序。
    # 后来发现想法就不对。我的方法是将数据分到32个桶中，每一个桶是一个区间范围[2^i, 2^(i+1)-1]，但这样没有办法区别区间中间的数据乘以2之后大于该数值的数目。
    # 考虑现在遍历到3，需要判断之前的结果中是否存在6，知道下一个桶中的数据为[4, 7]，但是我直接加桶的个数就错了，因为4，5，6的数据也会被算在其中
    # 所以从值域进行统计是不可行的
    res, bit_cnt, exe_cnt = 0, [0] * 32, [0]*32
    for v in nums:
        i, n, neg = 0, 0, False
        if v < 0:
            neg = True
            v = -v

        while v:
            if v & 1: n += 1
            v >>= 1
            bit_cnt[i] += 1
            i += 1

        if n == 1:
            exe_cnt[i - 1] += 1
            res -= exe_cnt[i]

        if neg:
            res += exe_cnt[0] - exe_cnt[i]

        res += bit_cnt[i]

    return res

def reversePairs_using_bisect_left(nums):
    # 参考：1）http://www.hawstein.com/posts/binary-indexed-trees.html 2）https://leetcode.com/problems/reverse-pairs/discuss/97268/General-principles-behind-problems-similar-to-%22Reverse-Pairs%22
    # 问题的本质上遍历到一个数据v，需要判断之前是否存在大于2*v的数据在已经遍历的集合中。想到bit tree的统计特性，问题是，如果统计值域，空间消耗太大。
    # 转过来想，只要计算排名高于2*v的数据即可，所以改成对**排名进行统计**。所以时间复杂度为O(4*n*log(n))，其中第一个log(n)是二分找排名，第二个log(n)是根据
    # 计算排名，第三个log(n)是找到v的排名，第四个log(n)是数据放入到BIT中

    # 实现BIT的时候有几个注意点：
    # - 一定要使用`bitset_left`，这样子可以保证，在集合中的数据，数据范围在[0, n)之间，便于update操作。而`2*v+1`之后的数据，可能比任何一个数值都大，也就是无效的排名，那么该数据在read时候不会计算(while判断)
    # - 计算2倍数值时，使用`2*v+1`，这样子可以保证是大于2*v的，符合题目要求
    # - 二分的结果要加1，这是因为BIT实现的要求，数据从1开始统计
    # - 使用`v & -v`来得到最低有效位的数值
    # - VIP：这里实现和传统的BIT逻辑**刚好相反**。传统的BIT是从0开始统计，这样子计算read的坐标不断缩小，而update则需要不断向上累加。而这里反过来，因为我们需要知道的是大于当前数值的个数，所以要对着n-1的位置看。
    #   所以，read的操作是不断增加的，而update的操作不断减小

    # 使用`biset_right`实现的结果是不对的。如果使用right操作，比如[2, 2, 100]，对2和50计算，都得到2结果，这不可以有效的说明其相关的排序关系。
    res, sorted_nums, n = 0, sorted(nums), len(nums)
    bit_tree = [0] * (n+1)

    def index(v):
        import bisect
        return bisect.bisect_left(sorted_nums, v) + 1

    def read(sorted_index):
        # 如果sorted_index过大，那么不会计算
        sum = 0
        while sorted_index < len(bit_tree):
            sum += bit_tree[sorted_index]
            sorted_index += sorted_index & -sorted_index
        return sum

    def update(sorted_index):
        while sorted_index > 0:
            bit_tree[sorted_index] += 1
            sorted_index -= sorted_index & -sorted_index

    for v in nums:
        res += read(index(2*v+1))
        update(index(v))

    return res

def reversePairs_using_bisect_right_not_correct(nums):
    res, sorted_nums, n = 0, sorted(nums), len(nums)
    bit_tree = [0] * (n+1)

    def index(v):
        import bisect
        res = bisect.bisect_right(sorted_nums, v)
        return res+1 if res < n else res

    def read(sorted_index):
        sum = 0
        while sorted_index < len(bit_tree):
            sum += bit_tree[sorted_index]
            sorted_index += sorted_index & -sorted_index
        return sum

    def update(sorted_index):
        while sorted_index > 0:
            bit_tree[sorted_index] += 1
            sorted_index -= sorted_index & -sorted_index

    for v in nums:
        res += read(index(2*v))
        update(index(v))

    return res

def reversePairs_using_self_impl_binary_search(nums):
    res, sorted_nums, n = 0, sorted(nums), len(nums)
    bit_tree = [0] * (n+1)

    def index(v):
        # 需要注意边界值
        l, r = 0, n
        while l < r:
            m = l + ((r-l)>>1)
            if sorted_nums[m] < v:
                l = m+1
            else:
                r = m
        return r+1

    def read(sorted_index):
        sum = 0
        while sorted_index < len(bit_tree):
            sum += bit_tree[sorted_index]
            sorted_index += sorted_index & -sorted_index
        return sum

    def update(sorted_index):
        while sorted_index > 0:
            bit_tree[sorted_index] += 1
            sorted_index -= sorted_index & -sorted_index

    for v in nums:
        res += read(index(2*v+1))
        update(index(v))

    return res

def reversePairs_using_merge_sort(nums):
    n = len(nums)
    buffer = [None] * n

    # 最本质的方法其实应该想到使用merge_sort，因为天然的思考过程可以考虑到分为两个部分
    # reversePairs的个数等于左边reverse的和右边reverse的，然后加上合并过程中reverse的
    # 这和merge_sort的过程不谋而和。实现的过程中，控制左边变量i的移动，每次找到一个i
    # 不停的移动p指针找到符合要求节点的上限，使用j指针找到比i节点小的节点上限，合并和
    # 计算reverse pair过程重叠，非常nice的solution
    def merge_sort_impl(l, r):
        if l >= r: return 0

        m = l + ((r-l)>>1)
        res = merge_sort_impl(l, m) + merge_sort_impl(m+1, r)

        i, j, p, k = l, m+1, m+1, 0
        while i <= m:
            while p <= r and nums[i] > nums[p]*2: p+=1
            res += p-m-1

            # 后面的小，取后面先
            while j <= r and nums[i] > nums[j]: buffer[k], j, k = nums[j], j+1, k+1

            # 左边的小，取前面节点
            buffer[k], k, i = nums[i], k+1, i+1

        while j <= r: buffer[k], j, k = nums[j], j+1, k+1
        nums[l:r+1] = buffer[:k]
        return res

    return merge_sort_impl(0, n-1)

def reversePairs_using_bst_tree(nums):
    """会TLE，如果树不平衡的话，退化为线性搜索"""
    class Node:
        def __init__(self, v, left=None, right=None):
            self.val = v

            # cnt初始值为1，因为节点本身记录cnt，创建的时候就包含了一次
            self.cnt = 1
            self.left = left
            self.right = right

    class BSTTree:
        def __init__(self):
            self.root = None

        def insert(self, v):
            self.root = self._insert_dfs(self.root, v)

        # BST实现时候的尾递归技巧，将root传入，然后返回当前insert之后的root
        # 如果root是空，创建节点，上层可以得到最新的root。如果不是，根据节点关系，递归构造，同时维护left和right的关系，最后返回root
        # 注意这里保存的cnt表示大于等于当前节点的个数。如果只是大于，会存在问题，比如搜索大于4的，结果搜索到节点是5，但是5自身的数值无法记录。
        # 所以BST记录数据**一定要保存自己的数值**
        def _insert_dfs(self, root, v):
            if not root:
                return Node(v)
            elif root.val == v:
                root.cnt += 1
            elif root.val < v:
                root.cnt += 1
                root.right = self._insert_dfs(root.right, v)
            else:
                root.left = self._insert_dfs(root.left, v)

            return root

        def search(self, v):
            return self._search_impl(self.root, v)

        # 搜索的时候，如果是左节点，需要加上当前的数值，因为当前根节点和右节点都大于当前数值。
        def _search_impl(self, root, v):
            if not root:
                return 0
            elif root.val == v:
                return root.cnt
            elif root.val < v:
                return self._search_impl(root.right, v)
            else:
                return root.cnt + self._search_impl(root.left, v)

    # 搜索使用2*v+1
    res, tree = 0, BSTTree()
    for v in nums:
        res += tree.search(2*v+1)
        tree.insert(v)

    return res


if __name__ == '__main__':
    print(reversePairs_using_self_impl_binary_search([5,4,3,2,1]))
    print(reversePairs_using_bisect_left([5,4,3,2,1]))
    print(reversePairs_using_merge_sort([-5, -5]))
    print(reversePairs_using_bst_tree([2,4,3,5,1]))
