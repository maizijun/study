import numpy as np

class Solution:
    
    def validTicTacToe(self, board) -> bool:

        ### numpy method ###
        arr1 = [k for k in board[0]]
        arr2 = [k for k in board[1]]
        arr3 = [k for k in board[2]]

        d = np.array([arr1,arr2,arr3])

        x_num = ('X'==d).sum().sum()
        o_num = ('O'==d).sum().sum()
        b_num = (' '==d).sum().sum()

        print(d)
        # return d


        x_win1 = any(np.all(d[:,k]=='X') for k in range(3))
        o_win1 = any(np.all(d[:,k]=='O') for k in range(3))

        x_win2 = any(np.all(d[k,:]=='X') for k in range(3))
        o_win2 = any(np.all(d[k,:]=='O') for k in range(3))

        x_win3 = all(np.all(d[k,k]=='X') for k in range(3))
        o_win3 = all(np.all(d[k,k]=='O') for k in range(3))

        x_win4 = all(np.all(d[k,2-k]=='X') for k in range(3))
        o_win4 = all(np.all(d[k,2-k]=='O') for k in range(3))

        print(x_win1,x_win2,x_win3,o_win1,o_win2,o_win3)
        x_win,o_win = any([x_win1,x_win2,x_win3,x_win4]),any([o_win1,o_win2,o_win3,o_win4])

        if x_num<o_num:
            return False
        
        if x_num>o_num+1:
            return False

        if x_num==o_num+1:
            if o_win:
                return False
            # elif b_num==9:
            #     return True
            else:
                return True

        if x_num==o_num:
            if x_win:
                return False
            elif o_win:
                return True
            else:
                return True

        
