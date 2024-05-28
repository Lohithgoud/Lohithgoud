class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary(nums,target,istrue):
            n = len(nums)
            left = 0
            right = n - 1
            idx = -1
            
            while left <= right:
                mid = (left + right) // 2 
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    idx = mid
                    if istrue:
                        right = mid - 1
                    else:
                        left = mid + 1
            return idx

        left = binary(nums,target,True)
        right = binary(nums,target,False)
        
        return [left,right]
            



# nums = [8]
        
