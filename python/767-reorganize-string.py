#/usr/bin/env python
#encoding: utf-8

'''
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].

- 使用贪心的策略，优先放数据最多的元素。如果放最小的，最多的后面将越来越不好放置。
- 使用优先队列实现最大的元素。
- 不过每次取得最大值之后，要将数据缓存一个回合，到下下轮才可以使用。
- 使用last_v, last_k来缓存数据，同时用sentinel模式来实现冷启动。
'''

class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        import heapq
        from collections import Counter
        res, q = [], [(-v, k) for k,v in Counter(S).items()]
        heapq.heapify(q)

        # 使用sentinel实现冷启动，之前的数据不需要考虑
        # 取出来的数据需要等到下一个回合才可以放到最大堆中
        last_v, last_k = 0, ''
        while q:
            v, k = heapq.heappop(q)
            if last_v < 0: heapq.heappush(q, (last_v, last_k))

            # 保存数据和去掉一个数据计数（负数所以是加1）一起实现，一气呵成
            last_v, last_k = v+1, k
            res.append(last_k)

        return ''.join(res) if last_v == 0 else ""