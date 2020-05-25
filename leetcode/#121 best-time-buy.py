class Solution:
    def maxProfit(self, prices):

        ## 找到买卖最优时间点 ##
        '''        
        p_min = prices[0]
        p_max = -99
        profit = -9999

        for p in prices[1:]:
            profit = max(profit,p-p_min) ## 此时的p_min都在p之前，能保证先后顺序逻辑
            p_min = min(p_min,p)
            p_max = max(p_max,p)

            print(profit,p_min,p_max)

            # p_max = max(p_max,p)
            # profit = p_max-p_min 不对的，因为p_max必须在p_min后面

        return result
            
        '''

        ## DP 算法 ##
        # status function: dp[i]=max(dp[i−1],prices[i]−minprice)

        if not prices:
            return 0

        max_profit = [0 for _ in prices]
        if len(prices)==2:
            return max(prices[1]-prices[0],0)
        else:
            p_min = prices[0]
            for ix,p in enumerate(prices[:]):
                if ix==0:
                    continue
                else:
                    max_profit[ix] = max(max_profit[ix-1],p-p_min)
                    p_min = min(p,p_min)

        return max_profit[-1]

a = Solution()
print(a.maxProfit([7,6,4,3,1]))
