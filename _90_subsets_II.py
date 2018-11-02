class Solution:

    def subsetsWithDupRecursive(self, S):
        if not S:
            return [[]]
        else:
            a = S[0]
            j = 1
            while j < len(S) and S[j] == a:
                j += 1
            Y = self.subsetsWithDupRecursive(S[j:])
            return Y + [
                [a] * k + y
                for y in Y
                for k in range(1, j+1)
            ]

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        return self.subsetsWithDupRecursive(nums)


s = Solution().subsetsWithDup([])
print(s)