#/usr/bin/env python
#encoding: utf-8

'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1

- 和数值相关的选择问题，使用dp进行状态保存。
- 这种dp一般将数值范围作为一个维度。
- 取多次数据的建模方式是：**从左到右对数值进行遍历，后面数值就用到前面数值多次取的结果**
- 看似二维dp，其实对j数值遍历，只需要得到前置数据大小，同时，同步修改最新数据，所以是1D的dp问题。
- dp[j] = min(dp[j], (dp[j-v] + 1) if j>=v)，这里的关键是min操作，这样子只要运行过的i和j保证最小，**串联起来就是全局最优**
- dp的核心就是用空间换时间，遍历一次，就可以将**历史最优信息保存下来，这样后面计算可复用之前信息，而不需要回头**
- 设计dp时候也需要考虑这种**连续最优的信息性质**

另外一个方法是使用备忘录方法：

- 对于有递归子结构的问题（当前问题可以根据递归子结构进行求解）都可以用备忘录方法加速dfs的搜索
- 理解时候，脑子中有一棵树的概念，每次搜索都是对一个树的完全剖析
- 实现时，大概结构是：1）初始化数据 2）dfs，如果存在mem，使用mem 3）对所有子情况进行分析，得到最优解，记做mem，加速下一次重复的dfs
- 区别好临界状态。用python实现会超时，可能和python递归实现比较消耗有关。
'''

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        import sys
        dp = [sys.maxsize] * (amount+1)
        dp[0] = 0

        for v in coins:
            for j in range(1, amount+1):
                if j >= v:
                    dp[j] = min(dp[j], dp[j-v]+1)

        return -1 if dp[amount] == sys.maxsize else dp[amount]

    def coinChangeTopDown(self, coins, amount):
        if amount <= 0: return 0
        import sys
        mem = [0] * amount
        def dfs(coins, amount, mem):
            # 边界条件很重要，如果amount小于0，表示找不到，返回-1.
            # 如果为0，这样子可以让上一层的节点自己本身进入解集合。
            if amount < 0: return -1
            if amount == 0: return 0

            # 0表示没有设置，需要和-1进行区别
            if mem[amount-1] != 0: return mem[amount-1]

            # 递归搜索所有子情况
            min_v = sys.maxsize
            for v in coins:
                res = dfs(coins, amount-v, mem)
                if res >= 0: min_v = min(min_v, res+1)

            # 如果一个有效解都不存在，记录为-1，表示找不到
            mem[amount-1] = -1 if min_v == sys.maxsize else min_v
            return mem[amount-1]

        dfs(coins, amount, mem)
        return mem[amount-1] if mem[amount-1] > 0 else -1