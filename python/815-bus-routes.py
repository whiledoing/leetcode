#/usr/bin/env python
#encoding: utf-8

"""
We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.

We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.

Example:
Input:
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
Output: 2
Explanation:
The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
Note:

1 <= routes.length <= 500.
1 <= routes[i].length <= 500.
0 <= routes[i][j] < 10 ^ 6.

- 图连接很多的时候，不一定非要使用传统的图数据结构保存数据，只要建立其节点和邻接节点对应关系即可，比如这里只是**保存反向的route索引**
- 层次遍历可以简写成下面的格式：每次生成一个新的queue，使用一句话的列表综合很舒服
- 将已经遍历的节点进行保存，这样子不会重复计算
"""
def numBusesToDestination(routes, S, T):
    """
    :type routes: List[List[int]]
    :type S: int
    :type T: int
    :rtype: int
    """
    if S == T: return 0

    # 不一定图一定就是建立连通节点，只要可以记录当前点的连接性质即可。
    # 所以这里使用反向的index建立信息，将点和对应的route的槽位进行匹配。
    from collections import defaultdict
    to_route = defaultdict(set)
    for i, route in enumerate(routes):
        for j in route:
            to_route[j].add(i)

    queue, cnt, visited = [S], 0, {S}
    while queue:
        # 1）从queue中取得当前层的节点 2）将节点连接的route_index取出来，这里使用pop操作，这样子运行过一次的节点，以后不会再次运行）
        # 3) 将route_index对应的连接点放入到下一层遍历的队列中
        if T in visited: return cnt
        queue = [next_node for cur_node in queue for route_index in to_route.pop(cur_node, []) for next_node in routes[route_index] if next_node not in visited]
        visited.update(queue)
        cnt += 1

    return -1