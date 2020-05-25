class Solution:
    def stoneGame(self, piles):
        ## dymamic programming ## 跟 minimax 没有半毛钱关系

        def range_sum(i,j): ## 表示i,j区间内能取到的最大值

            if i==j:
                return piles[i]
            else:
                # print(piles[i] + sum(piles[i+1:j+1]) - range_sum(i+1,j))
                # print(piles[j] + sum(piles[i:j]) - range_sum(i,j-1))
                return max(piles[i] + sum(piles[i+1:j+1]) - range_sum(i+1,j),
                        piles[j] + sum(piles[i:j]) - range_sum(i,j-1))

        max_point = range_sum(0,len(piles)-1)
        print(max_point)
        return max_point > sum(piles)/2

a = Solution()
print(a.stoneGame([7,7,12,16,41,48,41,48,11,9,34,2,44,30,27,12,11,39,31,8,23,11,47,25,15,23,4,17,11,50,16,
# 50,38,34,48,27,16,24,22,48,50,10,26,27,9,43,13,42,46,24
]))