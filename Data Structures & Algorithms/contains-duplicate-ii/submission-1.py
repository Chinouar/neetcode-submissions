class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        h = {}
        while i < len(nums):
            if nums[i] in h:
                for x in h.get(nums[i]):
                    if abs(x - i) <= k:
                        return True
                h[nums[i]].append(i)
            else:
                h[nums[i]] = [i]
            i+=1
        return False