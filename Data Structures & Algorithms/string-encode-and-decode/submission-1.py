class Solution:

    def encode(self, strs: List[str]) -> str:
        tmp = ""
        for i in strs:
            tmp += i
            tmp += 'é'
        return tmp

    def decode(self, s: str) -> List[str]:
        res = []
        tmp = ""
        for i in s:
            if i != 'é':
                tmp += i
            else:
                res.append(tmp)
                tmp = ""
        return res
