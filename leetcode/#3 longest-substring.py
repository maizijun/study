class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        word_set = set()
        len_all,len_tmp = 0,0
        st,ed = 0,0
        
        for x in s:
            if x not in word_set:
                word_set.add(x)
                len_tmp += 1
                ed += 1
                
            else:
                while(x in word_set):
                    # print(x in word_set,x,word_set)
                    word_set.remove(s[st])
                    len_tmp -= 1
                    st += 1
                    
                word_set.add(x)
                len_tmp += 1
                    
#             print(word_set)
            len_all = max(len_all,len_tmp)
     
        return len_all
                
    