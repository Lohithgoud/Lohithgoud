class Solution:
    def trap(self, arr: List[int]) -> int:
        n = len(arr)
        l = 0
        r = n - 1
        maxleft = maxright = 0
        res = 0 

        while l <= r :
            if arr[l] <= arr[r]:
                if arr[l] > maxleft:
                    maxleft = arr[l]
                else:
                    res += (maxleft - arr[l])
                l += 1
            else:
                if arr[r] > maxright:
                    maxright = arr[r]
                else:
                    res += (maxright - arr[r])
                r -= 1
        return res

        
