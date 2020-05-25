class Solution:
    def searchInsert(self, nums, target):

        ll = len(nums)
        # print(ll)

        if target <= nums[0]:
            return 0
        if target == nums[-1]:
            return ll-1
        if target > nums[-1]:
            return ll

        mid = nums[ll//2]

        if target==mid:
            return ll//2
        elif target<mid:
            nums = nums[:ll//2]
            return self.searchInsert(nums,target)
        else:
            nums = nums[ll//2+1:]
            return self.searchInsert(nums,target)+ll//2+1

a = Solution()
print(a.searchInsert([1,3,5,6],5))

        






