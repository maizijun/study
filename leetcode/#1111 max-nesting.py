#### 根本看不懂题目说个啥 ####
## 2020-05-25 又开始看懂一点了 ##

class Solution:
    def maxDepthAfterSplit(self, seq):

        # res = ['' for _ in seq]
        # close = [1,1]  ## 1代表闭合括号，-1代表不闭合
        # left_n,right_n = 0,0

        # for ix,s in enumerate(seq):
        #     if s=='(':
        #         if close[0]==1: #0闭合时，增加0
        #             res[ix]=0
        #             close[0] = -1
        #             left_n += 1
        #         elif left_n>right_n:
        #             res[ix]=1
        #             close[1] = -1
        #             right_n += 1
        #         else:
        #             res[ix]=0
        #             close[0] = -1
        #             left_n += 1

        #     if s==')':
        #         if close[0]==-1: #展开
        #             res[ix]=0
        #             close[0] = 1
        #             left_n -= 1
        #         else:
        #             res[ix]=1
        #             close[1] = 1
        #             right_n -= 1
            
            # print(res)

        '''
        我原来的思路:先上0括号，再上1括号，若1括号闭合了，则继续使用1括号，0括号闭合则使用0
        遇到的badcase：
        ((())) 当0展开，1展开时，还需要记录turn设定下一个到底是上0还是1，然后对应闭合也要记录是0或是1

        聪明人的思路：
        1.使用stack，记录每个括号对的层级，然后使得相邻层级，不会同时为0或1
        2.依次遍历字符串，若字符串相同，则赋值不同，若字符串不同，则赋值相同，很好的解决了(())和()()的问题
        '''
        res = [0 for _ in seq]
        for ix in range(1,len(seq)):
            if seq[ix]==seq[ix-1]:
                res[ix] = 1-res[ix-1]
            else:
                res[ix] = res[ix-1]

        return res

a = Solution()
print(a.maxDepthAfterSplit("((()))"))

        







