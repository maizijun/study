class Solution:
    def climbStairs(self, n):

        '''
        状态方程 dp[i] = dp[i-1] + dp[i-2] 
        '''

        res = [0 for _ in range(n+1)]
        for nn in range(n+1):
            if nn==0:
                pass
            elif nn==1:
                res[nn]=1
            elif nn==2:
                res[nn]=2
            else:
                res[nn] = res[nn-2] + res[nn-1]

        return res[-1]

a = Solution()
print(a.climbStairs(4))

