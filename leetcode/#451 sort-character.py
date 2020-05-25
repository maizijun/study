class Solution:
    def frequencySort(self, s: str) -> str:

        str_dict = {}

        for ss in s:
            str_dict[ss] = str_dict.get(ss,0) + 1

        print(str_dict)

        import heapq
        h = []
        for k,v in str_dict.items():
            heapq.heappush(h,v)

        h1 = []
        while(h):
            h1.append(heapq.heappop(h))
            print(h1)
        h = h1[::-1]
        str_order = heapq.nlargest(len(str_dict),str_dict.keys(),str_dict.get)

        print(str_order)
        print(h)

        return ''.join([ss*n for ss,n in zip(str_order,h)])

a = Solution()
print(a.frequencySort('raaeaedere'))
        