class Solution: 
    def rob1(self, arr: List[int]) -> int:
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
        
        
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        return max(self.rob1(nums[1:]),self.rob1(nums[:n-1]))

        
