class Solution:
    def topKFrequent(self, nums, k):

        n_times = dict()
        h = []

        import heapq
        for x in nums:
 
            n_times[x] = n_times.get(x,0) + 1

        print(n_times)
            
        for k_,v in n_times.items():
            print(h)
            if len(h)<k:
                heapq.heappush(h,v)
            elif v > h[0]:
                heapq.heappushpop(h,v)
            else:
                continue

        print(h)

        return heapq.nlargest(k,n_times.keys(),key=n_times.get)



a = Solution()
print(a.topKFrequent(nums = [5,3,1,1,1,3,73,1], k = 2))
                

            

            



