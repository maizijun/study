# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):

        if not root:
            return []

        res_all = []
        cur_level = [root]
        depth = 0

        while(cur_level):
            depth += 1
            # print(cur_level)

            res = []
            tmp = []
            for leaf in cur_level:

                if leaf.left:
                    tmp.append(leaf.left)
                if leaf.right:
                    tmp.append(leaf.right)

                res.append(leaf.val)
                # print(res)
                # res.reverse()

            if depth%2==0:
                res.reverse()
                
            cur_level = tmp
            res_all.append(res)

        return res_all
        
