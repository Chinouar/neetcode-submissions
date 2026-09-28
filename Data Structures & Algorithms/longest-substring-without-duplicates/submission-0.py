class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        best = 0
        for i, x in enumerate(s):
            while x in seen:
                seen.remove(s[left])
                left += 1
            seen.add(x)
            best = max(best, i - left + 1)
        return best