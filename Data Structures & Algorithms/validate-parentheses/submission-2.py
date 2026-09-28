from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        st = deque()
        for c in s:
            if c == '(' or c == '{' or c == '[':
                st.append(c)
            if c == ')' and (len(st) == 0 or st.pop() != '('):
                return False
            if c == '}' and (len(st) == 0 or st.pop() != '{'):
                return False
            if c == ']' and (len(st) == 0 or st.pop() != '['):
                return False
        return True if len(st) == 0 else False