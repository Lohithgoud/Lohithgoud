class Solution:
    def lcs(self,n,m,t1,t2,dp):
        if n < 0 or m < 0:
            return 0
        if dp[n][m] != -1:
            return dp[n][m]
        if t1[n] == t2[m]:
            dp[n][m] =  1 + self.lcs(n - 1,m - 1,t1,t2,dp)
        else:
            dp [n][m] = max(self.lcs(n - 1,m,t1,t2,dp),self.lcs(n,m - 1,t1,t2,dp))
        return dp[n][m]


    def longestCommonSubsequence(self, t1: str, t2: str) -> int:

        n = len(t1)
        m = len(t2)
        dp = [[-1 for j in range(m)]for i in range(n)]

        return self.lcs(n-1,m-1,t1,t2 , dp)

        
