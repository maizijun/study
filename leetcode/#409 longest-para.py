class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        if len(s)==1:
            return 1
        
        letter = {}
        for ss in s:
            letter[ss] = letter.get(ss,0)+1
            
        n=0
        is_odd = False
        print(letter)

        for v in letter.values():
            if v%2==0:
                n += v
            else:
                n += v-1
                is_odd = True
        
        return n+1 if is_odd else n
    
    
a = Solution()
print(a.longestPalindrome('abccccdd'))