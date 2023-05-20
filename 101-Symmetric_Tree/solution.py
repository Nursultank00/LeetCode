# Рекурсивно проверяем симметричность правого с левым (кросс)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.Symm(root.left, root.right)

    def Symm(self, a, b):
        if not a and not b:
            return True
        if a and b and a.val == b.val:
            return self.Symm(a.left, b.right) and self.Symm(a.right, b.left)
        return False