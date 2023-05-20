# Преордер проход root-left-right, разделяем с помощью #

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        result = []
        
        def helper(root):
            if root:
                result.append(root.val)
                helper(root.left)
                helper(root.right)
        helper(root)
        return "#".join(map(str, result))

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        numbers = [int(num) for num in data.split("#")]
        def helper(low, high):
            if numbers and low < numbers[0] < high:
                root_value = numbers.pop(0)
                root_node = TreeNode(root_value)
                root_node.left = helper(low, root_value)
                root_node.right = helper(root_value, high)
                return root_node
        return helper(-inf, inf)
