class Solution:
    def jump(self, nums) -> int:

        max_dis = 0
        k = 1
        n_times = {}
        n = len(nums)

        if n<=1:
            return 0

        if nums[0]>=n:
            return 1

        for i,num in enumerate(nums[:-1]):
            print(i,num)

            if i>max_dis:
                break
            if max_dis<i+num:
                if i+num>=n-1:
                    return n_times[i]+1

                else:
                    max_dis = i+num
                    n_times[max_dis]=k
                    k+=1
            print('max_dis',max_dis,'k:',k)
            print(n_times)
            
            # if max_dis>=n-1:
            #     return n_times[max_dis]

        # print(n_times)

a = Solution()
# print(a.jump([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]))
print(a.jump([2,3,1,1,4]))