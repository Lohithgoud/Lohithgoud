#User function Template for python3

class Solution:
    # nction to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        
        dp = [[0 for _ in range(W + 1)] for _ in range(n)]
        
        for i in range(wt[0],W + 1):
            dp[0][i] = val[0]
                
        
        
        for idx in range(1,n):
            for w in range(1,W + 1):
                notake = 0 + dp[idx - 1][w]
                
                take = float('-inf')
                
                if wt[idx] <= w:
                    take = val[idx] + dp[idx - 1][w - wt[idx]]
                    
                dp[idx][w] = max(take , notake)
        
        return dp[n - 1][W]
