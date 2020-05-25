class Solution:
    def countCharacters(self, words, chars):

        char_dict = {}
        for char in chars:
            char_dict[char] = char_dict.get(char,0) + 1


        def is_word(word):
            char_dict_tmp = char_dict.copy()

            for w in word:
                if char_dict_tmp.get(w,0)==0:
                    return 0
                else:
                    char_dict_tmp[w] -= 1

            return len(word)


        return sum([is_word(word) for word in words])


a = Solution()
print(a.countCharacters(words = ["hello","world","leetcode"], chars = "welldonehoneyr"))