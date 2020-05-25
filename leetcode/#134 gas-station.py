class Solution:
    ''' 
    题目的关键是理解，当到达t没油时，可以从t+1开始尝试 
    若t没油，则t-k都是有油，若从任意t-k开始，则t还是没油，所以不需要尝试从t-k开始
    '''
    def canCompleteCircuit(self, gas, cost) -> int:

        begin = 0
        end = 0
        ix = 0

        while(ix<=len(gas)):
            gas_tmp = gas[begin:] + gas[:begin]
            cost_tmp = cost[begin:] + cost[:begin]

            g_total,c_total = 0,0
            for g,c in zip(gas_tmp,cost_tmp):
                print(g,c)
                g_total += g
                c_total += c

                if g_total < c_total:
                    print('switch')
                    begin = end+1
                    end = begin
                    break

                end += 1
            ix += 1
            if g_total >= c_total:
                return begin
        return -1

a = Solution()
print(a.canCompleteCircuit(gas  = [2,3,4],cost = [3,4,3]))



