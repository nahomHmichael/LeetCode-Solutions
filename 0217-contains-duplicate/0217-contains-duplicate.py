class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        elif len(nums) == 1:
            return False
        else:
            dup_dict = {}
            for i in nums:
                if i in dup_dict:
                    return True
                else:
                    dup_dict[i] = 1
        return False