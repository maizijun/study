class Solution:
    def threeSum(self, nums):

        nums.sort()
        ll = len(nums)
        res = []

        for k in range(ll-2):
            print(k)

            if k>0 and nums[k]==nums[k-1]:  ##对于第一个index的重复项
                continue
            
            tmp = -nums[k]
            st,ed = k+1,ll-1

            while(st<ed):
                if nums[st]+nums[ed]==tmp:
                    res.append([nums[k],nums[st],nums[ed]])
                    while st<ed and nums[st]==nums[st+1]: ## 对于后面2个index去除重复项 ##
                        st += 1
                    while ed>st and nums[ed]==nums[ed-1]:
                        ed -= 1
                    st += 1
                    ed -= 1
                elif nums[st]+nums[ed]<tmp:
                    st += 1
                else:
                    ed -= 1

        return res
            
a = Solution()
print(a.threeSum([0,0,0]))
