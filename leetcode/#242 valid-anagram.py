class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s = [x for x in s]
        s.sort()
        
        t = [x for x in t]
        t.sort()
        
        # print(s)
        # t.sort()
    
        return s==t 
    