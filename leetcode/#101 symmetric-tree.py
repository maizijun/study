# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

## recursive method ##
## == 表示取值相同且 类索引值相同 ##
from copy import deepcopy 
class Solution:
    def isSymmetric(self, root) -> bool:

        def symm(root):
            root2 = deepcopy(root)
            if not root2:
                return None
            print(root2.val)

            if root2.left and root2.right:
                root2.right,root2.left = symm(root2.left),symm(root2.right)
                # print('aaaa',root.left.val,root.right.val)
            else:
                root2.right,root2.left = symm(root2.left),symm(root2.right)

            return root2

        symm_tree = symm(root)
        # print(symm_tree.left.left.val)
        # print(root.left.left.val)
        # print(type(symm_tree),type(root))

        print(root.__dict__,symm_tree.__dict__)
        return root.__dict__ == symm_tree.__dict__



T = TreeNode(1)
T.left = TreeNode(2)
T.right = TreeNode(2)
# T.left.left = TreeNode(3)
# T.right.right = TreeNode(3)
# print(T.left.right.val)

a = Solution()
print(a.isSymmetric(T))


#### 参考答案 ####

# 递归
def isSymmetric(root: TreeNode) -> bool:
    def help(left, right):
        # left/right都为空节点
        if not left and not right:
            return True
        # left/right有一个为空
        if not (left and right):
            return False
        # 值是否相等
        if left.val != right.val:
            return False
        # 将左右字节对称递归比较
        return help(left.left, right.right) and help(left.right, right.left)
   
    return help(root.left, root.right) if root else True

# 迭代
def isSymmetric1(root: TreeNode) -> bool:
    # 如果root节点为空, 或则单个root节点, 则返回True
    if not root or (not root.left and not root.right):
        return True
    # 如果left和right只有一个节点为空, 则返回False
    if not (root.left and root.right):
        return False
    left = [root.left]
    right = [root.right]
    while left:
        leftNode = left.pop()
        rightNode = right.pop()
        
        # 如果节点不相等, 则返回False
        if leftNode.val != rightNode.val:
            return False
        
        # 将左子树的左节点和右子树的右节点写入left/right数组中
        if leftNode.left and rightNode.right:
            left.append(leftNode.left)
            right.append(rightNode.right)
        elif leftNode.left or rightNode.right:
            return False
        
        # 将左子树的右节点和右子树的左节点写入left/right数组中
        if leftNode.right and rightNode.left:
            left.append(leftNode.right)
            right.append(rightNode.left)
        elif leftNode.right or rightNode.left:
            return False
        
    return True

# 简化的迭代
from collections import deque
def isSymmetric2(root: TreeNode) -> bool:
    deq = deque([root, root])
    while deq:
        t1, t2 = deq.pop(), deq.pop()
        # 两个节点都为空, 则继续判断
        if not t1 and not t2: continue
        # 存在一个节点为空, 则为False
        if not(t1 and t2): return False
        if t1.val != t2.val: return False
        # t1, t2的左右节点, 要对称的写入双端队列中
        deq.append(t1.left)
        deq.append(t2.right)
        deq.append(t1.right)
        deq.append(t2.left)
        
    return True

