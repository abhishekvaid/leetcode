class Solution:

    def recursiveExist(self, board, i, j, visited, word, k):

        # visited.add((i, j))

        visited.append((i, j))

        if k == len(word):
            return True
        elif board[i][j] == word[k]:
            for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                i_, j_ = i + di, j + dj
                if 0 <= i_ < len(board) and 0 <= j_ < len(board[0]):
                    if (i_, j_) not in visited:
                        if self.recursiveExist(board, i_, j_, visited, word, k + 1):
                            return True
            if k + 1 == len(word):
                return True

        visited.remove((i, j))

        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.recursiveExist(board, i, j, [], word, 0):
                    return True
        return False


board = [["a"]]

board = [
    ["A", "B", "C", "E"],
    ["S", "F", "E", "S"],
    ["A", "D", "E", "E"]
]

s = Solution().exist(board, "ABCESEEEFS")
assert s

# s = Solution().exist(board, "ABCCED")
# assert s
# s = Solution().exist(board, "SEE")
# assert s
# s = Solution().exist(board, "ABCB")
# assert not s
