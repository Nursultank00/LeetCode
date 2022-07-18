# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
        inorder(root)
        if not ans:
            return True
        for i in range(1, len(ans)):
            if ans[i] <= ans[i-1]: return False
        return True