class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        res = set()
        for i in range(l):
            tmp = -nums[i]
            j = 0
            k = l - 1
            while j < l:
                if i == j:
                    j += 1
                    continue
                if i == k:
                    k -= 1
                    continue
                if j == k:
                    if l - j > k:
                        j += 1
                        continue
                    else:
                        k -= 1
                        continue
                if j >= l or k < 0:
                    break
                if tmp == nums[j] + nums[k]:
                    t = [nums[i], nums[j], nums[k]]
                    t.sort()
                    res.add(tuple(t))
                    j += 1
                    k -= 1
                elif tmp > nums[j] + nums[k]:
                    j += 1
                else:
                    k -= 1
        r = [list(x) for x in res]
        return r