# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #### from reference answers ####
    def generateTrees(self, n: int) -> List[TreeNode]:

        if n==0:
            return [None]
        if n==1:
            return [TreeNode(n)]

        
        def newtree(i,j):

            if i>j:
                return [None]

            tree_ls = []
            for k in range(i,j+1):

                left = newtree(i,k-1)
                right = newtree(k+1,j)

                for a in left:
                    for b in right:
                        root = TreeNode(k)
                        root.left = a
                        root.right = b

                        tree_ls.append(root)

            return tree_ls

        return newtree(1,n)

