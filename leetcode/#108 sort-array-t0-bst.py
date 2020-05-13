# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# print(3//2)

class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:

        n = len(nums)

        if n == 0:
            return None
        if n == 1:
            return TreeNode(nums[0])
        if n >= 2:
            root = TreeNode(nums[n//2])
            root.left = self.sortedArrayToBST(nums[:n//2])
            root.right = self.sortedArrayToBST(nums[n//2+1:])
        
        return root

a = Solution()
print(a.sortedArrayToBST([1,2,3]))