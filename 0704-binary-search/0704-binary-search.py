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
        
        def _search(nums,low,high):
            if low>=high:
                return -1
            mid = low + (high-low)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                return _search(nums,mid+1,high)
            else: 
                return _search(nums,low,mid)
        return _search(nums,0,len(nums))
            