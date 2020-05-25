class Solution:

    def subsets(self, nums):
        from itertools import permutations,combinations

        return [list(x) for k in range(len(nums)+1) for x in combinations(nums,k)]

a = Solution()
print(a.subsets([1,2,3]))

