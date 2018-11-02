from pprint import pprint


class Solution:

    def __init__(self):
        self.n = 0

    def isOkay(self, B, i, j):
        return not any(
            abs(row - i) == abs(col - j)
            for row, col in enumerate(B[:i])
        )

    def solveNQueenRecursive(self, B, i, remainingCols):
        if len(remainingCols) == 0:
            self.n += 1
        else:
            for col in remainingCols:
                if self.isOkay(B, i, col):
                    remainingCols.remove(col)
                    B[i] = col
                    self.solveNQueenRecursive(B, i + 1, remainingCols)
                    remainingCols.add(col)
                    B[i] = -1

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        B = [-1] * n
        self.solveNQueenRecursive(B, 0, set(range(n)))
        return self.n


solution = Solution()
print(solution.totalNQueens(12))
