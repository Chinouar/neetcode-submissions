class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for i in strs:
            alpha = [0] * 26
            for j in i:
                alpha[ord(j) - 97] += 1
            alpha = str(alpha)
            if alpha not in h:
                h[alpha] = []
            h[alpha].append(i)
        return list(h.values())