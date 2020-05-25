class Solution:
    def maxSubArray(self, nums):
        
        '''3指针法'''
        st,ed,ix = 0,0,0
        gain = nums[0]
        
        if len(nums)==1:
            return nums[0]

        for ix in range(len(nums)):
            print(st,ed,ix,gain)

            if sum(nums[st:ix+1])>0:
                if gain < sum(nums[st:ix+1]):
                    gain = sum(nums[st:ix+1])
                    ed = ix                   

            if sum(nums[st:ix+1])<=0:
                if gain < sum(nums[st:ix+1]):
                    gain = sum(nums[st:ix+1])
                st = ix+1
                ed = ix+1

            
            print(st,ed,ix+1,gain)
            print('########################')
        
        return gain

a = Solution()
# print(a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(a.maxSubArray([-1,0]))


        #### 分治法 怎么使用 ####
