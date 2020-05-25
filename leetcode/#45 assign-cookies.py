class Solution:
    def findContentChildren(self, g, s) -> int:

        happy = 0
        g.sort()
        s.sort()

        for cookie in s:
            for user in g:
                if cookie >= user:
                    print(cookie,user)
                    happy += 1

                    g = g[1:]
                    break                    

        return happy

a = Solution()
print(a.findContentChildren([1,2], [1,2,3]))
