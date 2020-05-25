class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix:
            return False

        height = len(matrix)
        width = len(matrix[0])

        if height==0 or width==0:
            return False

        # 这是不对的，因为i+1行的开头值，可能小于i行值，所以对每一行都进行二分查找 #
        # if matrix[0][0]>target:
        #     return False
        # if matrix[height-1][width-1]<target:
        #     return False

        # for h in range(height-1):
        #     if matrix[h][0]<=target and matrix[h+1][0]>target:
        #         break
        #     else:
        #         continue


        # return h

        def find_mid(array,target):
            n = len(array)
            st,ed = 0,n  # 左闭右开

            if n == 1:
                if array[0]==target:
                    return True
                else:
                    return False

            else:
                mid = (st+ed)//2

                print(st,ed,mid)
                # print(array[mid]==target)
                if array[mid]==target:
                    return True

                elif target<array[mid]:
                    return find_mid(array[st:mid],target)
                else:
                    return find_mid(array[mid:ed],target)


        for h in range(height):
            # h表示第几个数组，然后在数组内寻找 #
            array = matrix[h]
            print(array)
            if find_mid(array,target):
                return True

        return False


        
matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]


a = Solution()
print(a.searchMatrix(matrix,20))
# print(matrix)



