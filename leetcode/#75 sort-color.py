class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """

        #### sort color #### 原地排序 不添加额外空间 双指针

        ll = len(nums)
        zero_ix = ix = 0
        two_ix = ll-1

        # for ix,val in enumerate(nums):  ## bad case: [1,2,0]
        while(ix<=two_ix):
            # print(zero_ix,ix,two_ix)
            # print(nums)

            if nums[ix] == 0:
                nums[zero_ix],nums[ix] = nums[ix],nums[zero_ix]
                zero_ix += 1
                ix += 1

            elif nums[ix] == 2:
                nums[two_ix],nums[ix] = nums[ix],nums[two_ix]
                two_ix -= 1

            else:
                ix += 1

            print(nums)
        return nums

a = Solution()
print(a.sortColors([1,2,0]))

        


