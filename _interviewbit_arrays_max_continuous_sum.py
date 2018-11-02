import sys


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        maxEndingHere, maxNum = A[0], A[0]
        for a in A[1:]:
            maxEndingHere = max(maxEndingHere + a, a)
            maxNum = max(maxEndingHere, maxNum)
        return maxNum

A = [-2,1,-3,4,-1,2,1,-5,4]
s = Solution().maxSubArray(A)
assert s == 6