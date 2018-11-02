from collections import defaultdict


class Trie:

    def __init__(self, word=None):
        """
        Initialize your data structure here.
        """
        self.word = None
        self.count = 0
        self.D = defaultdict(Trie)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        root = self
        for ch in word:
            root = root.D[ch]

        root.word = word
        root.count += 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        try:
            root = self
            for ch in word:
                root = root.D[ch]
        except KeyError as e:
            return False

        return root.word is not None

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        try:
            root = self
            for ch in prefix:
                root = root.D[ch]
        except KeyError as e:
            return False

        return True

    def consume(self, w):
        return self.D[w]

    def has(self, ch):
        return ch in self.D


class Solution:

    def __init__(self):
        self.T = Trie()
        self.Accumulator = set()

    def makeTrie(self, words):
        for w in words:
            self.T.insert(w)

    def dfs(self, board, i, j, visited, trieRoot):

        if trieRoot.has(board[i][j]):
            trieRoot_ = trieRoot.consume(board[i][j])
            if trieRoot_.word is not None:
                self.Accumulator.add(trieRoot_.word)
            for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                i_, j_ = di+i, dj+j
                if 0 <= i_ < len(board) and 0 <= j_ < len(board[0]):
                    if not (i_, j_) in visited:
                        visited.add((i_, j_))
                        self.dfs(board, i_, j_, visited, trieRoot_)

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.makeTrie(words)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, set(), self.T)
        return list(self.Accumulator)


words = ["oath", "pea", "eat", "rain"]
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

words = ["aaa"]
board = [
    ["a", "a"]
]

words = ["a"]
board = [
    ["a"]
]

s = Solution()
print(s.findWords(board, words))
