class Solution:
    def func(self,i,j,arr,dp):
        if i == 0 and j == 0:
            if arr[i][j] != 1:
                return 1
            else:
                return 0
        if i < 0 or j <  0:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]
        
        up = ryt = 0
        if arr[i][j] != 1:
            up = self.func(i-1,j,arr,dp)
            ryt = self.func(i,j-1,arr,dp)

        dp[i][j] = up + ryt

        return dp[i][j]


    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp =[[-1 for _ in range(n)] for _ in range(m)]
        return self.func(m-1,n-1,grid , dp)
        
