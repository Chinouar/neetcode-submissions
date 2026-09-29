import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            k = (left + right) // 2
            tmp = sum(math.ceil(p / k) for p in piles)
            if tmp <= h:
                right = k
            else:
                left = k + 1
        return left


