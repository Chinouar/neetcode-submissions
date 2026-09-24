class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = dict.fromkeys(nums, 1)
        m = 0
        print(h)
        for x in nums:
            if x - 1 not in h.keys():
                tmp = 1
                seq = x
                while seq+1 in h:
                    tmp += 1
                    seq += 1
                if m < tmp:
                    m = tmp
        return m