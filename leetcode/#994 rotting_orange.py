class Solution:
    def orangesRotting(self, grid):

        if grid = [[0]]:
            return 0

        height = len(grid)
        width = len(grid[0])

        queue = []
        is_rot = []
        is_orange = []

        for h in range(height):
            for w in range(width):
                if grid[h][w]==2:
                    is_rot.append((h,w))
                if grid[h][w]==1:
                    is_orange.append((h,w))

        queue += is_rot

        def is_board(h,w):
            return w>=0 and w<=width-1 and h>=0 and h<=height-1

        n_time = 0
        while(queue):
            # print(grid)
            queue = []
            for h,w in is_rot:
                for w_tmp,h_tmp in [(w-1,h),(w+1,h),(w,h-1),(w,h+1)]:

                    if is_board(h_tmp,w_tmp) and grid[h_tmp][w_tmp]==1 and (h_tmp,w_tmp) not in queue:
                        grid[h_tmp][w_tmp]=2
                        is_orange.remove((h_tmp,w_tmp))
                        queue.append((h_tmp,w_tmp))
            
            is_rot = queue.copy()
            
            n_time += 1

            print(queue)
            print(n_time)
        print(is_orange)

        return -1 if is_orange else n_time-1


a = Solution()
print(a.orangesRotting([[0,2]]))