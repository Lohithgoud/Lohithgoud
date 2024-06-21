class Solution:
    def func(self,i,j,m,n,dp):
        if i == 0 and j == 0:
            return 1
        if i < 0 or j < 0:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        up = self.func(i-1,j,m,n,dp)
        ryt = self.func(i,j-1,m,n,dp)

        dp[i][j] = up + ryt
        return dp[i][j] 



    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]
        return self.func(m-1,n-1,m,n,dp)
        
