class Solution:
    def longestPalindrome(self,s):
        if len(s)==1:
            return s

        # How can we reuse a previously computed palindrome to compute a larger palindrome?
        ## 这个题目还是不错的 ##

        # n = len(s)
        # dp = [[False] * n for _ in range(n)]
        # ans = ""
        # # 枚举子串的长度 l+1
        # for l in range(n):
        #     # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
        #     for i in range(n):
        #         j = i + l
        #         if j >= len(s):
        #             break
        #         if l == 0:
        #             dp[i][j] = True
        #         elif l == 1:
        #             dp[i][j] = (s[i] == s[j])
        #         else:
        #             dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
        #         if dp[i][j] and l + 1 > len(ans):
        #             ans = s[i:j+1]
        # return ans

        ## 是否可以用另一个状态方程判断呢 使用n^2时间复杂度 ##
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        length = -1

        res = ''

        for _ in range(n):
            for i in range(n): # 开始index
                for j in range(i,n):  # 结束index(1,3)的先后顺序先于(2,2)，不符合，原答案按照字符长度从小到大较合适 
                    
                    if i==j:  #同一个
                        dp[i][j] = True
                    elif i+1==j:  #相邻
                        dp[i][j] = True if s[i]==s[j] else False
                    else:
                        dp[i][j] = dp[i+1][j-1] and s[i]==s[j]
                        
                    if dp[i][j] and j-i>length:
                        res = s[i:j+1]  
                        length = j-i
                    print(i,j,dp[i][j])
        # print(dp)

        return res

a = Solution()
print(a.longestPalindrome("ab"))




