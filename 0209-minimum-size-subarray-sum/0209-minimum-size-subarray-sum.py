class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        tot = 0
        result = float("inf")
        for r in range(len(nums)):
            tot += nums[r]
            while tot >= target:
                result = min(r-l + 1, result)
                tot -= nums[l]
                l += 1
        return 0 if result == float("inf") else result