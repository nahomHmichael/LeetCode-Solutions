class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            m = abs(i)
            if nums[m-1]<0:
                res.append(m)
            else:
                nums[m-1]*=-1
        return res