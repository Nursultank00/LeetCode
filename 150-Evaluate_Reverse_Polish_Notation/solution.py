# Используем стек

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item in ("*", "/", "+", "-"):
                second = stack.pop()
                first = stack.pop()
                result = 0
                if item == "*":
                    result = first * second
                elif item == "/":
                    result = int(first/second)
                elif item == "-":
                    result = first - second
                elif item == "+":
                    result = first + second
                stack.append(result)
            else:
                stack.append(int(item))
        return stack[0]