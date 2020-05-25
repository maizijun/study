class Solution:
    def generateParenthesis(self, n):
        ## somehow good problem ##

        ## 枚举法 ## 俗称回溯法？？
        '''
        列出所有括号的情况，使用balance变量（#左括号-#右括号），
        若balance>=0，表示是有效的括号组合
        可使用dfs方法遍历

        example:
        def dfs(s,a,b):
            s：已有的字符
            a: 使用了左括号的数目
            b: 使用了右括号的数目
        '''

        ## 动态规划法 ##
        '''
        以第一个左括号（为切入点，找到对应的结束右括号），判断里面有多少个完整括号
        最少0个，最多n-1个
        '''
        res_dict = {}
        res_dict[0]=['']
        res_dict[1]=['()']

        if n==0:
            # return ''
            pass
        if n==1:
            # return ['()']
            pass
        if n>=2:
            for num in range(2,n+1): ## num个括号组
                res = []

                for l_pth in range(num): ## 第一个括号内的括号数目
                    # print(num,l_pth)
                    # print(res_dict[l_pth],res_dict[num-l_pth-1])

                    for pre_left in res_dict[l_pth]:
                        for pre_right in res_dict[num-l_pth-1]:
                            left_pth = '(' + pre_left + ')'
                            right_pth = pre_right

                            # print(left_pth)
                            # print(right_pth)
                            # print(left_pth+right_pth)
                            res.append(left_pth+right_pth)

                # print(res)
                res_dict[num] = res

        return res_dict[num]

a = Solution()
print(a.generateParenthesis(4))



