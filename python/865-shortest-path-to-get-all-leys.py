"""
We are given a 2-dimensional grid. "." is an empty cell, "#" is a wall, "@" is the starting point, ("a", "b", ...) are keys, and ("A", "B", ...) are locks.

We start at the starting point, and one move consists of walking one space in one of the 4 cardinal directions.  We cannot walk outside the grid, or walk into a wall.  If we walk over a key, we pick it up.  We can't walk over a lock unless we have the corresponding key.

For some 1 <= K <= 6, there is exactly one lowercase and one uppercase letter of the first K letters of the English alphabet in the grid.  This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys.  If it's impossible, return -1.



Example 1:

Input: ["@.a.#","###.#","b.A.B"]
Output: 8
Example 2:

Input: ["@..aA","..B#.","....b"]
Output: 6


Note:

1 <= grid.length <= 30
1 <= grid[0].length <= 30
grid[i][j] contains only '.', '#', '@', 'a'-'f' and 'A'-'F'
The number of keys is in [1, 6].  Each key has a different letter and opens exactly one lock.

其实就是地图的bfs扫描，只是正常的bfs需要记录visited只是记录当前节点是否被扫描过, 而这里代入了状态，如果每次进入一个节点拥有的key列表不一样，那么还需要重新扫描遍历：

- 之所以不用dfs是因为这里计算的是移动路径的最小值，dfs可以得到结果，但不一定是最小值，需要全局遍历所有路径才知道最小值，而bfs天然的可以得到当前计算的层级
- 时间复杂度是O(kmn)，其实m,n是grid的维度，k表示钥匙的个数，可以理解为对所有的行动状态进行遍历。
- 记录获取钥匙状态可以用mask（有限状态的存在问题），提高计算效率
"""


def shortestPathAllKeys(self, grid):
    """
    :type grid: List[str]
    :rtype: int
    """
    q, target, visited, level = [], 0, {}, 1
    lower_letter, upper_letter = 'abcdef', 'ABCDEF'
    dire = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    m, n = len(grid), len(grid[0])
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == '@':
                q.append((i, row.index('@'), 0))
                visited[q[0]] = True
            elif c in lower_letter:
                target += 1

    # 注意移位操作的优先级超级低，所以用括号组合
    target = (1 << target) - 1
    while q:
        new_q = []
        for ori_i, ori_j, keys_mask in q:
            for i_c, j_c in dire:
                i, j = ori_i + i_c, ori_j + j_c
                if i < 0 or i >= m: continue
                if j < 0 or j >= n: continue

                c = grid[i][j]
                if c == '#': continue

                loc = (i, j, keys_mask)
                if loc in visited: continue

                # 有限的状态使用mask来标记效果更好，检测是否可以通过当前锁
                if c in upper_letter and keys_mask & (1 << (ord(c)-ord('A'))) == 0:
                    continue

                if c in lower_letter:
                    index = ord(c) - ord('a')
                    new_keys_mask = keys_mask | (1 << index)
                    if new_keys_mask == target: return level
                    loc = (i, j, new_keys_mask)

                new_q.append(loc)
                visited[loc] = True

        level += 1
        q = new_q

    return -1