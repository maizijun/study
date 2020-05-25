class Solution:
    def search(self, nums, target) -> int:

        ll = len(nums)

        if not nums:
            return -1

        if target==nums[0]:
            return 0
        if target==nums[-1]:
            return ll-1

        if len(nums)==1:
            if nums[0]!=target:
                return -1

        if len(nums)==2:
            if target != nums[0] and target == nums[1]:
                return -1

        


        mid = ll//2
        if target == nums[mid]:
            return mid
        else:
            print(nums)

            if target < nums[0] and target > nums[-1]: ## 在旋转位置的空隙
                return -1 

            if nums[mid] > nums[0]: ## 目标 > 初始点，表示左半段为大
                if target > nums[0] and target < nums[mid]:
                    nums = nums[:mid]
                    return self.search(nums,target)
                else:
                    nums = nums[mid+1:]
                    return self.search(nums,target) + mid+1 if self.search(nums,target)!=-1 else -1
            else: ## 目标 < 结束点，表示右半段为小
                if target > nums[mid] and target < nums[-1]:
                    nums = nums[mid+1:]
                    return self.search(nums,target) + mid+1 if self.search(nums,target)!=-1 else -1
                else:
                    nums = nums[:mid]
                    return self.search(nums,target)
            


a = Solution()
print(a.search(nums = [7,8,1,2,3,4,5,6], target = 2))

        

