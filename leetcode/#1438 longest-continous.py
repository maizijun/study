class Solution:
    def longestSubarray(self, nums,limit):

        if not nums:
            return 0

        array_min = nums[0]
        array_max = nums[0]
        ix1 = ix2 = 0
        res = nums[:1]
        max_len = 1
        tmp_len = 1

        for value in nums[1:]:
            # print(max_len)
            res.append(value)
            tmp_len += 1

            # print(res)

            if abs(value-array_max)<=limit and abs(value-array_min)<=limit:
                ix2 += 1
                array_max = max(array_max,value)
                array_min = min(array_min,value)

                max_len = max(max_len,tmp_len)

            else:
                ix2 += 1
                # while (abs(value-array_max)>limit or abs(value-array_min)>limit): # 不需要while，因为我们已经有了暂定的max，
                # 对于长度小于max的情况，不需要进行考虑，所以ix1+1即可，不需要遍历ix+...
                ix1 += 1
                res.pop(0)
                array_max = max(res)
                array_min = min(res)
                tmp_len -= 1



            # print('after process:',res)

        return max_len


a = Solution()
print(a.longestSubarray([4,2,2,2,4,4,2,2],2))




#### 这是个啥 ####
class Solution(object):
    def longestSubarray(self, nums, limit):
        if not nums:
            return 0
        curr_max = nums[0] # 当子数组下最大值 这里初始化为第一个数
        curr_min = nums[0] # 当子数组下最大值 这里初始化为第一个数
        sub_nums = [] # 以数组作为窗口滑动
        for num in nums:
            if abs(num - curr_max) <=  limit and abs(num - curr_min) <=  limit and abs(curr_max - curr_min) <= limit:
                curr_max = max(num,curr_max)
                curr_min = min(num,curr_min)
                sub_nums.append(num)
            else:    
                sub_nums.append(num)
                sub_nums.pop(0)
                curr_max = max(sub_nums) # 当子数组最大值
                curr_min = min(sub_nums) # 当前子数组最小值
        return  len(sub_nums)

