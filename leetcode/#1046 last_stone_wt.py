class Solution:
    def lastStoneWeight(self, stones):

        stones.sort()
        print(stones)

        if len(stones)==1:
            return stones[0]

        elif len(stones)==2:
            return stones[-1]-stones[-2]

        else:
            tmp = stones[-1]-stones[-2]
            stones.remove(stones[-1])
            stones.remove(stones[-1])
            stones.append(tmp)

            return self.lastStoneWeight(stones)
