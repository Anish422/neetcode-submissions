class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix        # store product of everything left of i
            prefix *= nums[i]      # then include nums[i] for the next spot

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix       # multiply in everything right of i
            suffix *= nums[i]

        return res