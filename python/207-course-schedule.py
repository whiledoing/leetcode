#/usr/bin/env python
#encoding: utf-8

'''
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.

就是寻找是否有环图，权当复习了一下：

- 使用bfs：1）将图的所有入度为0的点放到队列中 2）对队列中每个元素进行bfs 3）将相邻的点都取出，去掉入度，如果入度为0，放入队列
- 使用dfs：1）使用visited表示是否访问过节点 2）使用path来记录路径 3）注意visited和path不一样，有的节点visited了，不一定在path上。
'''
class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        e = [[] for _ in range(numCourses)]
        for p1, p2 in prerequisites:
            e[p2].append(p1)
        return not self.iscyclic(e, numCourses)

    def iscyclic(self, e, numCourses):
        path, visited = set(), set()
        def dfs(e, start):
            if start in visited: return False
            visited.add(start)
            path.add(start)
            for p in e[start]:
                if p in path or dfs(e, p): return True
            path.remove(start)
            return False

        return any(dfs(e, start) for start in range(numCourses) if start not in visited)

    def canFinish_using_bfs(self, numCourses, prerequisites):
        A = [[] for i in range(numCourses)]
        for edge in prerequisites:
            A[edge[1]].append(edge[0])

        numIncomingEdges = [0]*numCourses
        for edge in prerequisites:
            numIncomingEdges[edge[0]] += 1

        S = []
        for n in range(numCourses):
            if numIncomingEdges[n] == 0:
                S.append(n)
        while len(S) > 0:
            n = S.pop()
            for m in A[n]:
                numIncomingEdges[m] -= 1
                if numIncomingEdges[m] <= 0:
                    S.append(m)

        return sum(numIncomingEdges) == 0