#User function Template for python3

class Solution:
    def fun(self,n,t,arr,dp):
        
        if t == 0:
            return True
            
        if n == 0:
            return arr[0] == t
            
        if dp[n][t] != -1:
            return dp[n][t]
            
        notake = self.fun(n-1,t,arr,dp)
        
        take = False
        
        if arr[n] <= t:
            take = self.fun(n-1,t - arr[n],arr,dp)
            
        dp[n][t] = take or notake
        
        return dp[n][t]
        
    def isSubsetSum (self, N, arr, t):
        # code here 
        dp = [[-1 for _ in range(t + 1)] for _ in range(N +1 )]
        
        return self.fun(N-1,t,arr,dp)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends
