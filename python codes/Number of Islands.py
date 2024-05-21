from collections import deque

class Solution:
    def dfs(self,row,col,visit,grid):
        q = deque()
        visit[row][col] = True
        q.append((row,col))
        dirc = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            row,col = q.popleft()
            for drow,dcol in dirc:
                nrow = row + drow
                ncol = col + dcol
                if(0 <= nrow < len(grid) and 0 <= ncol < len(grid[0]) and grid[nrow][ncol] == "1" and visit[nrow][ncol] == False):
                    visit[nrow][ncol] = True
                    q.append((nrow,ncol))


    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0
        visit = [[False]*m for _ in range(n)]

        for row in range(n):
            for col in range(m):
                if(visit[row][col] == False and grid[row][col] == "1"):
                    res += 1
                    self.dfs(row,col,visit,grid)
        return res
