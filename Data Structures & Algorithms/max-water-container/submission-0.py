class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0
        l = len(heights)
        j = l-1
        i = 0
        while i < l:
            tmp = (j - i) * min(heights[i], heights[j])
            m = tmp if tmp > m else m
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        return m
