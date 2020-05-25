# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        else:
            res = [root.val]

        up_t = [root]
        down_t = []

        while(up_t):
            for t in up_t:
                if not (t.left or t.right):
                    continue
                if t.left:
                    down_t.append(t.left)
                if t.right:
                    down_t.append(t.right)

            if down_t:
                res.append(down_t[-1].val)
                print(down_t[-1])
            up_t = down_t
            down_t = []

        return res



