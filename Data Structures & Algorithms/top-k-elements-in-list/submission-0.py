class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for i in nums:
            h[i] = 1 + h.get(i, 0)
        res = []
        while k > 0:
            m = max(h,key=h.get)
            res.append(m)
            h[m] = 0
            k -= 1
        return res
