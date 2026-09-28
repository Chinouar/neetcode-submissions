class MinStack:

    def __init__(self):
        self.st = []
        self.l = 0
        self.mini = []

    def push(self, val: int) -> None:
        self.st.append(val)
        self.l += 1
        if self.mini:
            self.mini.append(min(self.mini[-1], val))
        else:
            self.mini.append(val)

    def pop(self) -> None:
        self.l -= 1
        self.st.pop()
        self.mini.pop()

    def top(self) -> int:
        return self.st[self.l - 1]

    def getMin(self) -> int:
        return self.mini[-1]
        
