class Solution:
    def search(self, nums: List[int], k: int) -> int:
        if len(nums)  == 0:
            return -1
            
        n = len(nums)
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid =(low + high) // 2
            if nums[mid] == k:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= k and nums[mid] >= k :
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= k and nums[high] >= k :
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
