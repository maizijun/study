class Solution:
    
    def __init__(self, nums):
        self.nums = nums
        

    def pick(self, target):
        import numpy as np

        max_num = 1

        for ix,x in enumerate(self.nums):
            if x==target:
                rand = np.random.randint(0,max_num)
                if rand == 0:
                    reser = ix
                max_num += 1

        return reser
        
# import numpy as np
# print(np.random.randint(0,0.5))

# Your Solution object will be instantiated and called as such:
obj = Solution([1,2,3,3])
param_1 = obj.pick(3)
print(param_1)