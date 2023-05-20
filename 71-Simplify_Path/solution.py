# Сплит по слешу, и делаем условия добавления в стек

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for item in path.split("/"):
            if item in (".", ""):
                pass
            elif item == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(item)
        return "/" + "/".join(stack)