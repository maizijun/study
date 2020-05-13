class Solution:
    def largestSumAfterKNegations(self, A, K) -> int:

        neg_nums = len([*filter(lambda x:x<=0,A)])
        print(neg_nums)

        A.sort()

        if K==0:
            return sum(A)
        if K<=neg_nums:
            A[:K] = map(lambda x:-x,A[:K])
            return sum(A)
        if K>neg_nums:
            A[:neg_nums] = map(lambda x:-x,A[:neg_nums])

            A.sort()

            K2 = K-neg_nums
            if K2%2==1:
                A[0] = -A[0]

            return sum(A) 

a = Solution()
print(a.largestSumAfterKNegations([-2,9,9,8,4],5))
print(a.largestSumAfterKNegations([2,3,4],1))
