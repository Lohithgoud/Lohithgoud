#User function Template for python3

class Solution:
    def fun(self,idx,n,price,dp):
        if idx == 0:
            return price[0] * n
            
        if dp[idx][n] != -1:
            return dp[idx][n]
        
        notake = 0 + self.fun(idx-1,n,price,dp)
        
        take = float('-inf')
        rod = idx + 1 
        if  rod <= n:
            take = price[idx] + self.fun(idx,n - rod,price,dp)
        
        dp[idx][n] =  max(take,notake)
        return dp [idx][n]

        
        
    def cutRod(self, price, n):
        #code here
        dp = [[-1 for _ in range(n+1)] for _ in range(n)]
        return self.fun(n-1,n,price,dp)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
