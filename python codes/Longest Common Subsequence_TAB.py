class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:

        n = len(t1)
        m = len(t2)

        dp = [[-1 for j in range(m + 1)] for i in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0
        
        for j in range( m + 1):
            dp[0][j] = 0

        for id1 in range(1,n + 1):
            for id2 in range(1,m + 1):
                if(t1[id1 - 1] == t2[id2 - 1]):
                    dp[id1][id2] = 1 + dp[id1 -1][id2 - 1]
                else:
                    dp[id1][id2] = max(dp[id1 - 1][id2], dp[id1][id2 - 1])

        return dp[n][m]



        
