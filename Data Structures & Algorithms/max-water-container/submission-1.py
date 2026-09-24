class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0
        l = len(heights) - 1
        j = l-1
        i = 0
        while i < l:
            tmp = (l - i) * min(heights[i], heights[l])
            m = tmp if tmp > m else m
            if heights[i] <= heights[l]:
                i += 1
            else:
                l -= 1
        return m
