# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q) -> bool:
        
        if (p==None) & (q==None):
            return True
        if (p!=None) & (q==None):
            return False
        if (p==None) & (q!=None):
            return False

        if p.val!=q.val:
            return False
        else:
            if self.isSameTree(p.left,q.left) & self.isSameTree(p.right,q.right):
                return True
            else:
                return False
                