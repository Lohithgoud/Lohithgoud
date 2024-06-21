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
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0 :
                     dp[0][0] = 1
                else:
                    up = ryt = 0
                    if i > 0:
                        up = dp[i-1][j]
                    if j > 0:
                        ryt = dp[i][j-1]
                    
                    dp[i][j] = up + ryt
            
        return dp[m-1][n-1]
