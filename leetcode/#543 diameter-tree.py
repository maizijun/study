# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0

        def depth(root):
            if not root:
                return 0
            if root.left is None and root.right is None:
                return 1
            if root.left is not None and root.right is None:
                return 1 + depth(root.left)
            if root.right is not None and root.left is None:
                return 1 + depth(root.right)
            if root.left is not None and root.right is not None:
                return 1 + max(depth(root.left),depth(root.right))

        return max(depth(root.left)+depth(root.right)+1,
                    self.diameterOfBinaryTree(root.left),
                    self.diameterOfBinaryTree(root.right))

print(max(1,2,3))