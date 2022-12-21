class Solution:
    def search(self, nums: List[int], target: int) -> int:
#         left, right =0, len(nums)-1
        
#         while left <= right:
#             mid = (left + right)//2
            
            
#             if nums[mid] > target:
#                 right = mid - 1
                
#             elif nums[mid] < target:
#                 left = mid +1 
                
#             else: 
#                 return mid
#         return -1
        
        def rec (nums,low,high): 
            if low>=high:
                return -1
            mid = low + (high-low)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                return rec(nums,mid+1,high)
            else: 
                return rec(nums,low,mid)
        return rec(nums,0,len(nums))
            