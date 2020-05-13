import heapq

class KthLargest:
    
    def __init__(self, k: int, nums):
        self.h = nums
        self.k = k
        # for x in nums:
        #     heapq.heappush(self.h,x)
        #     print(self.h)
        self.pool = heapq.nlargest(k,self.h)[::-1]


    def add(self, val: int) -> int:

        if len(self.pool) < self.k:
            heapq.heappush(self.pool,val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool,val)
        else:
            pass

        # heapq.heappush(self.h,val)
        # return heapq.nlargest(self.k,self.h)[-1]

        return self.pool[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k=2, nums=[4,5,8,2])
# param_1 = obj.add(val)