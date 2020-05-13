# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        # if root.left is None and root.right is not None:
        #     root.left,root.right = root.right,None
        # elif root.left is not None and root.right is None:
        #     root.right,root.left = root.left,None
        # elif root.left is None and root.right is None:
        #     root.left,root.right = None,None

        if not root:
            return None
        else:
            root.left,root.right = root.right,root.left
            root.left = self.invertTree(root.left)
            root.right = self.invertTree(root.right)
        
        return root 