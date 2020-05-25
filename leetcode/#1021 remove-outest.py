class Solution:
    def removeOuterParentheses(self, S):

        res = ''
        stack = []

        for value in S:
            if value=='(':
                stack.append(value)
                if len(stack)>1:
                    res += value
            else:
                if len(stack)>1:
                    stack.pop()
                    res += value
                else:
                    stack.pop()

            print(res)
        return res

a = Solution()
print(a.removeOuterParentheses("(()())(())(()(()))"))




