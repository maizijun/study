class Solution:
    def majorityElement(self, nums):

        counter_dict = {}
        for x in nums:
            counter_dict[x] = counter_dict.get(x,0) + 1

        l = len(nums)

        re = [k for k,v in counter_dict.items() if v>=l/2] 
        print(re)

        return re[0]

a = Solution()
print(a.majorityElement([3,2,3]))