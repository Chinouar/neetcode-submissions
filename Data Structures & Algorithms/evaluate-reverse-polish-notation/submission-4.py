from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        operators = deque()
        for s in tokens:
            if s == '+' or s == '-' or s == '*' or s == '/':
                #print(operands)
                num2 = int(operands.pop())
                num1 = int(operands.pop())
                match s:
                    case '+':
                        tmp = num1 + num2
                        #print(tmp)
                        operands.append(tmp)
                    case '-':
                        tmp = num1 - num2
                        #print(tmp)
                        operands.append(tmp)
                    case '*':
                        tmp = num1 * num2
                        #print(tmp)
                        operands.append(tmp)
                    case '/':
                        tmp = num1 / num2
                        #print(tmp)
                        operands.append(tmp)
            else:
                operands.append(s)
        return int(operands.pop())