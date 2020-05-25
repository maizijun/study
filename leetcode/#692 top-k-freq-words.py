from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words, k):

        word_dict = Counter(words)

        h = [[-freq,word,freq] for word,freq in word_dict.items()]
        heapq.heapify(h)

        print(h)
        print(heapq.nsmallest(3,h,lambda x:x[1]))

        return [heapq.heappop(h)[1:] for _ in range(k)]


# class Solution(object):

#     def topKFrequent(self, words, k):
#         count = Counter(words)
#         candidates = count.keys()
        
#         count.(key = lambda w: (-count[w], w))
#         return candidates[:k]


a = Solution()
print(a.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], k = 0))