# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):

        if not root:
            return 0

        elif not root.right and not root.left:
            return 1
        
        elif root.left and root.right:
            return min(1+self.minDepth(root.left), 1+self.minDepth(root.right))

        elif root.left:
            return 1+self.minDepth(root.left)

        else:
            return 1+self.minDepth(root.right)


        

        

