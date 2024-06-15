class Solution:
    
    def rob(self, arr: List[int]) -> int:
        n = len(arr)
        prev = arr[0]
        prev2 = 0

        for i in range(1, n):
            pick = arr[i]
            if i > 1:
                pick += prev2
            nonPick = 0 + prev

            cur_i = max(pick, nonPick)
            prev2 = prev
            prev = cur_i

        return prev
        
        
