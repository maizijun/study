class Solution:
    def canJump(self, nums) -> bool:
        # print(nums)
        
        length = len(nums)
        
        if length==1:
            return True
        
        if (nums[0] == 0) & (length>1) :
            return False
        
        for ix in range(1,length):
            
            # print(ix)
            
            if nums[length-ix-1] >= ix:
                return self.canJump(nums[:length-ix])
            
        return False

#### 从前往后 顺序法 ####
#### 每次记录能达到的最大坐标 ####
class Solution:
    def canJump(self,nums):

        n = len(nums)
        max_dis = 0

        if n==1:
            return True
        
        if (nums[0] == 0) & (n>1) :
            return False

        for i,num in enumerate(nums):
            if i>max_dis:
                break
            
            if max_dis>=i and n-i<=nums[i]:
                return True
            
            if max_dis>=i and i+num>=max_dis:
                max_dis = i+num            
            
        return max_dis >= n-1



