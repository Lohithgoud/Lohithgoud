class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = float('-inf')
        sum = 0
        for i in range(n):
            sum += nums[i]

            if maxi < sum:
                maxi = sum

            if sum < 0:
                sum = 0
                
        return maxi
