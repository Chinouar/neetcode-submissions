class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h = {}
        l = 0
        max_freq = 0
        best = 0
        for r, c in enumerate(s):
            h[c] = h.get(c, 0) + 1
            max_freq = max(max_freq, h[c])
            while (r - l + 1) - max_freq > k:
                h[s[l]] -= 1
                l += 1
            best = max(best, r - l + 1)
        return best