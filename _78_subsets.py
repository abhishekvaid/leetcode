class Solution:

    def subsetsRecursive(self, S):
        if not S:
            return [[]]
        else:
            a = S[0]
            S = S[1:]
            Y = self.subsetsRecursive(S)
            return Y + [[a] + y for y in Y]

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.subsetsRecursive(nums)


s = Solution().subsets([1, 2, 3])
print(s)