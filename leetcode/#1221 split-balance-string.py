class Solution:
    def balancedStringSplit(self, s: str) -> int:

        num = 0
        while(len(s)>0):
            
            n1,n2 = 0,0

            X = s[0]
            y = ''
            n1 = 1

            for ss in s[1:]:

                if ss == X[0]:
                    n1 += 1
                    X += ss
                else:
                    n2 += 1
                    y += ss

                # print(ss,n1,n2)
                if n1 == n2:
                    break

            length = len(X)
            s = s[2*length:]

            num += 1

            # print(X,y)
        return num

a = Solution()
print(a.balancedStringSplit('RLRRRLLRLL'))

