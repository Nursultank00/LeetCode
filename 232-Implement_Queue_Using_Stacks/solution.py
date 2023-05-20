# O(1) push, O(1) амортизированное pop.

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def helper(self, stack):
        if not stack:
            while self.stack1:
                p = self.stack1.pop()
                stack.append(p)
    
    def pop(self) -> int:
        self.helper(self.stack2)
        return self.stack2.pop()

    def peek(self) -> int:
        self.helper(self.stack2)
        return self.stack2[-1]

    def empty(self) -> bool:
        return len(self.stack1)+len(self.stack2) == 0