#User function Template for python3

class Solution:
    def fun(self,idx,w,wt,val,dp):
        
        if idx == 0:
            if wt[0] <= w:
                return val[0]
            else:
                return 0
        
        if dp[idx][w] != -1:
            return dp[idx][w]
        
        notake = self.fun(idx - 1,w,wt,val,dp)
        take = float("-inf")
        
        if wt[idx] <= w:
            take = val[idx] + self.fun(idx-1,w - wt[idx] , wt,val,dp)
            
        dp[idx][w] = max(take,notake)
        
        return dp[idx][w]
                
        
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        
        dp = [[-1 for _ in range(W + 1)] for _ in range(n)]
        return self.fun(n - 1,W,wt,val,dp)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends
