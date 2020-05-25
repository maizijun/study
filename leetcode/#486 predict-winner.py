class Solution:
    def PredictTheWinner(self, nums):

        def range_sum(i,j): ## 表示i,j区间内能取到的最大值,i,j表示闭区间索引点

            if i==j:
                return nums[i]
            else:
                return max(nums[i] + sum(nums[i+1:j+1]) - range_sum(i+1,j),
                        nums[j] + sum(nums[i:j]) - range_sum(i,j-1))

            max_point = range_sum(0,len(nums)-1)

            return max_point

        if len(nums)%2==0:
            return True

        elif len(nums)==1:
            return True

        else:
            ll = len(nums)-1
            res = sum(nums) - min(range_sum(1,ll),range_sum(0,ll-1))
            print(res,sum(nums))
            return res > sum(nums)/2

a = Solution()
print(a.PredictTheWinner([ 5, 233,7]))