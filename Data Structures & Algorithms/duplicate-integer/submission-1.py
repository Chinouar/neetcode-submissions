class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = [0] * len(nums)
        for i in nums:
            tmp = nums.index(i)
            if check[tmp] == 1:
                return True
            else:
                check[tmp] = 1
        return False
        