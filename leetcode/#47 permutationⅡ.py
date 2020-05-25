class Solution:
    def permuteUnique(self, nums):

        #### backtrack ####

        res = []
        prefix = []
        suffix = []

        def helper(string,n):

            # if len(n)==0:
            if not n:
                res.append(string)
                return  ## 结束函数

            elif (string in prefix) and (n in suffix):
                return

            else:
                for ix in range(len(n)):
                    helper(string + [n[ix]],n[:ix]+n[ix+1:])
                    prefix.append(string + [n[ix]])
                    suffix.append(n[:ix]+n[ix+1:])

        helper([],nums)

        return res


a = Solution()
print(a.permuteUnique([1,1,1,2]))

# xx = [3,6,7]
# print(xx[:0])