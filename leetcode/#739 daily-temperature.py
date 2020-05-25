class Solution:
    def dailyTemperatures(self, T):

        l = len(T)
        res = [0]*l  ## 记录结果
        ix_ls = [] ## 记录每个进去数字的索引 

        for ix,val in enumerate(T):
            # print(ix_ls)

            if ix_ls and (val <= T[ix_ls[-1]]): ## 当新加入的温度不大于之前时，入栈，
                ix_ls.append(ix)

            else:
                while ix_ls and (val > T[ix_ls[-1]]): ## 当新加入温度A大于之前某个值时B，B出栈，继续判断直到B比剩余的小
                    res[ix_ls[-1]] = ix - ix_ls[-1]
                    ix_ls.pop()

                ix_ls.append(ix)

        return res

a = Solution()
print(a.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))







# temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# 你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
