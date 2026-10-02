class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = i = 0
        tmp = 0
        while i < len(nums):
            if nums[i] == 1:
                tmp += 1
            else:
                m = tmp if tmp > m else m
                tmp = 0
            i += 1
        m = tmp if tmp > m else m
        return m