import numpy as np
class Solution:
    def getLeastNumbers(self, arr, k: int):

        return np.sort(arr)[:k]

a = Solution()
print(a.getLeastNumbers([1,2,3],2))