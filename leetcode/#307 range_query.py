class NumArray:
    
    def __init__(self, nums):
        self.nums = nums        

    def update(self, i: int, val: int) -> None:
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[i:j+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)




class SegmentTree:
    def __init__(self, data, merge): 
        '''
        data:传入的数组
        merge:处理的业务逻辑，例如求和/最大值/最小值，lambda表达式
        '''
        self.data = data # [2,3,4,5,1]
        self.n = len(data) # 5 
        #  申请4倍data长度的空间来存线段树节点
        self.tree = [None] * (2 * self.n) # 索引i的左孩子索引为2i+1，右孩子为2i+2 里面存储节点值，为2个子节点和
        self._merge = merge # lambda x,y 
        if self.n:
            self._build(0, 0, self.n-1)  ## 递归了建立全部线段树 是BFS优先得到的字段序列


    def query(self, ql, qr):
        '''
        返回区间[ql,..,qr]的值
        '''
        return self._query(0, 0, self.n-1, ql, qr)


    def update(self, index, value):
        # 将data数组index位置的值更新为value,然后递归更新线段树中被影响的各节点的值
        self.data[index] = value
        self._update(0, 0, self.n-1, index)


    def _build(self, tree_index, l, r):
        '''
        递归创建线段树
        tree_index : 线段树节点在数组中位置
        l, r : 该节点表示的区间的左,右边界
        '''
        if l == r:
            self.tree[tree_index] = self.data[l]
            return
        mid = (l+r) // 2 # 区间中点,对应左孩子区间结束,右孩子区间开头
        left, right = 2 * tree_index + 1, 2 * tree_index + 2 # tree_index的左右子树索引
        self._build(left, l, mid)
        self._build(right, mid+1, r)
        self.tree[tree_index] = self._merge(self.tree[left], self.tree[right])


    def _query(self, tree_index, l, r, ql, qr):
        '''
        递归查询区间[ql,..,qr]的值
        tree_index : 某个根节点的索引
        l, r : 该节点表示的区间的左右边界
        ql, qr: 待查询区间的左右边界
        '''
        if l == ql and r == qr: # 总和
            return self.tree[tree_index] 

        mid = (l+r) // 2 # 区间中点,对应左孩子区间结束,右孩子区间开头
        left, right = tree_index * 2 + 1, tree_index * 2 + 2
        if qr <= mid:
            # 查询区间全在左子树
            return self._query(left, l, mid, ql, qr)
        elif ql > mid:
            # 查询区间全在右子树
            return self._query(right, mid+1, r, ql, qr)

        else: # 查询区间一部分在左子树一部分在右子树
            return self._merge(self._query(left, l, mid, ql, mid), 
                          self._query(right, mid+1, r, mid+1, qr))


    def _update(self, tree_index, l, r, index):
        '''
        tree_index:某个根节点索引
        l, r : 此根节点代表区间的左右边界
        index : 更新的值的索引
        '''
        if l == r == index:
            self.tree[tree_index] = self.data[index]
            return
        mid = (l+r)//2
        left, right = 2 * tree_index + 1, 2 * tree_index + 2
        if index > mid:
            # 要更新的区间在右子树
            self._update(right, mid+1, r, index)
        else:
            # 要更新的区间在左子树index<=mid
            self._update(left, l, mid, index)
        # 里面的小区间变化了，包裹的大区间也要更新
        self.tree[tree_index] = self._merge(self.tree[left], self.tree[right])
        

class NumArray:

    def __init__(self, nums):
        self.segment_tree = SegmentTree(nums, lambda x, y : x + y)
        

    def update(self, i: int, val: int) -> None:
        self.segment_tree.update(i, val)
        

    def sumRange(self, i: int, j: int) -> int:
        return self.segment_tree.query(i, j)
        

obj = NumArray([2,4,3,5,1])
# obj.update(i,val)
param_2 = obj.sumRange(0,4)
print(param_2)

# print(list(map(lambda x,y:x+y,[1,2,3,4,5])))