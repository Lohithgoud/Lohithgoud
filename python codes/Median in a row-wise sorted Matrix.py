#User function Template for python3

class Solution:
    def upperbond(self,arr,n,val):
        low = 0
        high = n-1
        
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] <= val:
                low = mid + 1
            else:
                high = mid - 1
                
        return low
    
    
    def median(self, matrix, r, c):
        
        low = 1
        high = 2001
            
        req = (r*c) // 2
        
        while low <= high:
            mid = (low + high) // 2
            
            count = 0
            for i in range(r):
                count += self.upperbond(matrix[i],c,mid)
            
            if count <= req:
                low = mid + 1
            else:
                high = mid - 1
                
        return low


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            t=[int(el) for el in input().split()]
            for j in range(c):
                matrix[i][j]=t[j]
        ans = ob.median(matrix, r, c);
        print(ans)
# } Driver Code Ends
