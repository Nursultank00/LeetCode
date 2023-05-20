class TreeNode:
    def __init__(self, value):
        self.val = value
        self.right = None
        self.left = None

d = {}

def inorder(root):
    if not root:
        return set()
    else:
        d[root] = inorder(root.left) | {root.val} | inorder(root.right)
        return d[root]

def equal(d):
    keys = list(d.keys())
    for i in range(len(keys)-1):
        for j in range(i+1, len(keys)):
            if d[keys[i]] == d[keys[j]]:
                return (keys[i], keys[j])