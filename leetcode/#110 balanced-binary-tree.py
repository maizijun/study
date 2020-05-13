# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def depth(self,root):
         
        if root==None:
            return 0
        else:
            return 1+max(self.depth(root.left),
            self.depth(root.right))    
    
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        elif (self.depth(root.left)-self.depth(root.right))**2<=1 and 
        self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else:
            return False


