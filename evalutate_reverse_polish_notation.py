class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for num in tokens:

            if num == "+" or num == "-" or num == "*" or num == "/":
                a = int(stack[-1])
                b = int(stack[-2])
                if num == "+": 
                    stack.pop()
                    stack[-1] = a + b
                elif num == "-":
                    stack.pop()
                    stack[-1] = b - a
                elif num == "*":
                    stack.pop()
                    stack[-1] = b * a
                elif num == "/":
                    stack.pop()
                    stack[-1] = int(b / a)
            else:
                stack.append(num)

        return int(stack[0])