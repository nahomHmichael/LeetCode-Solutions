class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res = [1] * (len (nums))
        # prefix = 1
        # for i in range (len (nums)):
        #     res[i] = prefix
        #     prefix *= nums [i]
        # postfix = 1
        # for i in range (len (nums) - 1, -1, -1):
        #     res[i] *= postfix
        #     postfix *= nums[i]
        # return res
        right_multiply = [0] * len(nums)
        right_multiply[-1]=nums[-1]
        for i in range(1,len(nums)):
            right_multiply[len(nums)-i-1] = right_multiply[len(nums)-i] * nums[len(nums)-i-1]
        output = [0]*len(nums)
        prefix = 1
        current_index = 0
        while current_index < len(output)-1:
            output[current_index] = prefix * right_multiply[current_index+1]
            prefix *= nums[current_index]
            current_index +=1
        output[-1] = prefix
        return output