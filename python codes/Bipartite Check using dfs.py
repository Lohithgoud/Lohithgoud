#leetcode,tuf

class Solution:
    def dfs(self, start, col, graph, colour):
        colour[start] = col
        for ngbr in graph[start]:
            if colour[ngbr] == -1:
                if not self.dfs(ngbr, 1 - col, graph, colour):
                    return False
            elif (colour[ngbr] == col):
                return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        v = len(graph)
        colour = [-1] * v
        for i in range(v):
            if colour[i] == -1:
                if  not self.dfs(i, 0, graph, colour):
                    return False

        return True
