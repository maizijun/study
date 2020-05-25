# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    #### 广度优先搜索思路 ####
    def largestValues(self, root):
        if not root:
            return []

        result = []

        q = [(root, 0)] ## 给定初始第0层节点与层数 ##

        while q:
            curr, level = q.pop(0) ## 获取第0层的节点 与 层数，此时q为空 ##

            if level == len(result):  ## 当层数 == result长度时，也即开始下一层遍历，将该层的初始数据加入 精彩！！##
                result.append(curr.val) 

            result[level] = max(result[level], curr.val)

            ## 添加下一层节点 ##
            if curr.left:
                q.append((curr.left, level + 1))
            if curr.right:
                q.append((curr.right, level + 1))
            
        return result

