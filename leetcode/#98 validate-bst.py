# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    #### 挺好的题目 ####
    def isValidBST(self, root):

        ## 这是不对的 ##
        # if not root:
        #     return True
        # elif root.left and root.right:
        #     return (root.val > root.left.val) and (root.val < root.right.val) and \
        #         self.isValidBST(root.left) and self.isValidBST(root.right)
        # elif root.left:
        #     return (root.val > root.left.val) and self.isValidBST(root.left)
        # elif root.right:
        #     return (root.val < root.right.val) and self.isValidBST(root.right)
        # else:
        #     return True

        ## method:使用中序遍历，比较遍历结果与排序结果 ## 

        ## method2: 定义判断大小函数 ##

        def helper(node,minn,maxx):
            if not node:
                return []

            if node.val >= maxx or node.val <= minn:
                return False

            if node.left and not helper(node.left,minn,node.val):
                return False
            if node.right and not helper(node.right,node.val,maxx):
                return False
            
            return True

        return helper(root,-1,999999999)
            


print(1e5)




