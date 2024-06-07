class Solution:
    def candy(self, arr: List[int]) -> int:
        n = len(arr)
        i = 1
        res = 1
        while( i < n):
            if arr[i] == arr[i-1]:
                res += 1 
                i += 1
                continue
            
            peak = 1
            while (i < n and arr[i] > arr[i - 1]):
                peak += 1
                res += peak
                i += 1

            down = 1
            while( i < n and arr[i]  < arr[i- 1]):
                res += down
                down += 1
                i += 1

            if down > peak:
                res += (down - peak)

        return res
            
        

        
