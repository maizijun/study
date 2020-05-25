class Solution:
    def removeDuplicates(self, nums):

        i,j = 1,1
        # n_unique = 1
        while(j<len(nums)):
            # print(i,j)
            # print(nums)

            if nums[i-1]==nums[j]:
                nums.pop(j)
            else:
                nums[i]=nums[j]
                print(nums)
                i+=1
                j+=1
                # n_unique += 1

        # nums = nums[:n_unique]
        print(nums)


a = Solution()
# a.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
a.removeDuplicates([1,1,2])





