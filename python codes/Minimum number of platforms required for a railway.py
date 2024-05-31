
class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        
        arr.sort()
        dep.sort()
        
        i = 1
        j = 0
        count = 1
        ans = 1
        
        while (i < len(arr)) and (j < len(dep)):
            
            if arr[i] <= dep[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
                
            ans = max(ans,count)
        
        return ans
