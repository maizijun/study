class Solution:
    def numTrees(self, n: int) -> int:

        if n==0:
            return 1
        if n==1:
            return 1
        if n==2:
            return 2
        # if n>=3:
        #     return sum([self.numTrees(k-1)*self.numTrees(n-k) for k in range(1,n+1)])

        #### 需要设置列表放置已有结果 ####
        r = [1,1,2]
        for i in range(3,n+1):
            # print(i)
            r.append(sum([r[k]*r[i-k-1] for k in range(i)]))

            # print(r)

a = Solution()
a.numTrees(19)