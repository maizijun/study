class Solution:
    def fourSum(self, nums, target):

        ## 4数之和，先排序，外层套2层循环，剩余2层使用双指针对应 ##

        ll = len(nums)        
        res = []
        nums.sort()

        for a in range(ll-3):
            for b in range(a+1,ll-2):

                target2 = target-nums[a]-nums[b]
                c = b+1
                d = ll-1

                while(c<d):                    
                    if nums[c]+nums[d]==target2:
                        # print('====match====')
                        if [nums[a],nums[b],nums[c],nums[d]] not in res:
                            res.append([nums[a],nums[b],nums[c],nums[d]])
                        c += 1
                        d -= 1
                        # print('after:',c,d)
                    elif nums[c]+nums[d]<target2:
                        c += 1
                    else:
                        d -= 1
                    
        return res

a = Solution()
print(a.fourSum(nums=[-3,-2,-1,0,0,1,2,3],target = 0))


