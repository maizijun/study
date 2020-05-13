class Solution:
    def isSubsequence(self, s, t) -> bool:

        len1 = len(s)
        len2 = len(t)

        if not s:
            return True

        ix = 0
        for x in t:
            if x == s[ix]:
                ix += 1

            if ix >= len1:
                return True

        return False

a = Solution()
s = 'abc'
t = ''
            

