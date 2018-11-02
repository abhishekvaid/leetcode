from pprint import pprint


class Solution:

    def __init__(self):
        self.Accumulator = []

    def isOkay(self, B, i, j):
        return not any(
            abs(row - i) == abs(col - j)
            for row, col in enumerate(B[:i])
        )

    def solveNQueenRecursive(self, B, i, remainingCols):
        if len(remainingCols) == 0:
            self.Accumulator.append(list(B))
        else:
            for col in remainingCols:
                if self.isOkay(B, i, col):
                    remainingCols.remove(col)
                    B[i] = col
                    self.solveNQueenRecursive(B, i + 1, remainingCols)
                    remainingCols.add(col)
                    B[i] = -1

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        B = [-1] * n
        self.solveNQueenRecursive(B, 0, set(range(n)))
        return self.makeOutput()

    def makeOutput(self):
        return [
            [
                "." * col + "Q" + "." * (len(board) - col - 1)
                for col in board
            ]
            for board in self.Accumulator
        ]


solution = Solution()
print(solution.solveNQueens(4))
print("\n\n".join("\n".join(ll) for ll in solution.makeOutput()))