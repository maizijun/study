class Solution:
    def letterCombinations(self, digits):
        ## 这不是很简单嘛，排列组合就行了 ## pythonic coding 
        
        num_letter_dict = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

        # string = ''

        # if len(digits)==0:
        #     return ''
        # elif len(digits)==1:
        #     return digits[1]

        #### 定义一个函数 不返回值，直接修改一个全局变量string ####

        res = []
        def helper(string,digits):
            if len(digits)==0:
                res.append(string)
                return None
            
            for s in num_letter_dict[digits[0]]:
                # print(s)
                # digits = 
                # string += s 不能进行=赋值？否则会影响其他循环内的赋值？
                # print(string)
                # print(digits,len(digits)==0)
                helper(string+s,digits[1:])

        helper('',digits)

        return res

a = Solution()
print(a.letterCombinations([2,3]))




#### official answer ####
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
                
        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map 
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])
                    
        output = []
        if digits:
            backtrack("", digits)
        return output




#### pythonic answer ####
class Solution:
    def letterCombinations(self, digits):
        conversion={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if len(digits)==0:
            return [] 
        product=['']
        for k in digits:
            product=[i+j for i in product for j in conversion[k]]
        return product


