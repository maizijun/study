class Solution:
    def missingNumber(self,nums):

        # for ix1,x in enumerate(nums):
        #         for y in range(ix1):
        #             if nums[ix1-y] < nums[ix1-y-1]:
        #                 nums[ix1-y],nums[ix1-y-1] = nums[ix1-y-1],nums[ix1-y]
        #             else:
        #                 break

        # print(nums)
        a = set(list(range(len(nums)+1)))
        b = set(nums)
        print(a)
        print(b)
        print(list(a-b))
        return list(a-b)[0]

a = Solution()
print(a.missingNumber([4,3,2,1]))




            

