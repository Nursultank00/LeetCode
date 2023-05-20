# Стек

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closure = {")": "(", "}": "{", "]": "["}
        for i in s:
            if i not in closure:
                stack.append(i)
            elif stack and closure[i] == stack[-1]:
                stack.pop()
            else:
                return False
        return len(stack) == 0