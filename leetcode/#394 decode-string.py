class Solution:
    def decodeString(self, s):

        ## good question ## 

        import re
        abc_rule = re.compile('[a-zA-Z]')
        num_rule = re.compile('[0-9]')
        x_int = 0
        stack = []
        res = ''

        ## 栈结构 ##
        ## 当遇到【，前面的字符与数字入栈，当遇到】，字符与数字出栈 ## 此处较难理解 太难懂了

        for x in s:
            if re.findall(num_rule,x):
                x_int = 10*x_int + int(x)
                print(x_int)

            elif x =='[':
                stack.append((res,x_int))
                x_int = 0
                res=''
                # continue

            elif re.findall(abc_rule,x):
                x_int = 0
                res += x #合并【后的字符串

            else: # 】出栈结果
                x_int = 0
                s_tmp,n_tmp = stack.pop()
                res = s_tmp + n_tmp*res

            print('stack:',stack)
            print('res:',res)

        return res




a = Solution()
# print(a.decodeString("2[abc]3[cd]ef"))
print(a.decodeString("3[a]2[b4[F]c]"))
        



## 牛逼的解法 ##
## 对于每个(数字)+(字母)的组合，append成字符串 ## 然后再组合(数字)+(字母) 逐步往外推
class Solution:
    def decodeString(self,s:str)->str:
        import re
        pattern=re.compile(r'(\d+)\[(\w+)\]')
        m=pattern.findall(s) 
        while m:
            for num,char in m:
                s=s.replace(f'{num}[{char}]',char*int(num))
            m=pattern.findall(s)
        return s

