from itertools import product
from pprint import pprint

class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not A[0]:
            return A
        else:
            nRow, nCol = len(A), len(A[0])
            A_ = [
                [0] * nRow
                for _ in range(nCol)
            ]
            for i, j in product(range(nRow), range(nCol)):
                A_[j][i] = A[i][j]
            return A_


A_ = Solution().transpose([[1,2,3],[4,5,6],[7,8,9]])
pprint(A_)