class Solution:
    def hammingDistance(self, x, y):

        ## &是按位且逻辑运算符
        ## |是按位或逻辑运算符
        ## ^是按位异或逻辑运算符

        return bin(x^y)[2:].count('1')

        # print(list(bin(11))[2:],list(bin(31))[2:])


a = Solution()
print(a.hammingDistance(11,14))