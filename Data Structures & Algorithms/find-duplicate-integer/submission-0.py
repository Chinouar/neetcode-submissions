class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        h = {}
        for x in nums:
            if x in h:
                return x
            else:
                h[x] = 1
        return 0