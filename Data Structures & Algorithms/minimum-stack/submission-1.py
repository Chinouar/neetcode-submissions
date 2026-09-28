class MinStack:

    def __init__(self):
        self.st = []
        self.l = 0
        self.mini = None

    def push(self, val: int) -> None:
        self.st.append(val)
        self.l += 1
        self.mini = val if self.mini == None or self.mini > val else self.mini

    def pop(self) -> None:
        self.l -= 1
        self.st.pop()

    def top(self) -> int:
        return self.st[self.l - 1]

    def getMin(self) -> int:
        return min(self.st)
        
