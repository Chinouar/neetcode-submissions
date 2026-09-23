class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = len(s)
        if not s or l == 1:
            return True
        j = l - 1
        i = 0
        while i < l/2:
            while not s[j].isalnum():
                j -= 1
                if j < 0:
                    return True
            while not s[i].isalnum():
                i += 1
                if i < l - 1:
                    return True
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
            
            