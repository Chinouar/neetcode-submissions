class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [1] * l
        tmp1 = 1
        for i in range(l):
            res[i] = tmp1
            tmp1 *= nums[i]
        tmp2 = 1
        for i in range(l - 1, -1, -1):
            res[i] *= tmp2
            tmp2 *= nums[i]
        return res
