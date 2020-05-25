# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        ## 使用rand7 * rand7 生成49点，选择4个1~10的点，有效提升效率 ##

        z = 0

        while(z==0):
            x = rand7()
            y = rand7()

            if x==4:
                continue
            elif x<=3:
                z = y
                return y
            else:
                if y>=4:
                    continue
                else:
                    z = y+7
                    return z
