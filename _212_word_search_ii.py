from collections import defaultdict


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.freq = 0
        self.word = None
        self.trie = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        root = self
        for ch in word:
            if ch not in root.trie:
                root.trie[ch] = Trie()
            root = root.trie[ch]
        root.word = word
        root.freq += 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        try:
            root = self
            for ch in word:
                root = root.trie[ch]
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
                root = root.trie[ch]
        except KeyError as e:
            return False

        return True

    def consume(self, w):
        return self.trie[w]

    def has(self, ch):
        return ch in self.trie


class Solution:

    def __init__(self):
        self.T = Trie()
        self.Accumulator = set()

    def makeTrie(self, words):
        for w in words:
            self.T.insert(w)

    def dfs(self, board, i, j, visited, trie):

        visited.add((i, j))
        if trie.has(board[i][j]):
            trie_ = trie.consume(board[i][j])
            if trie_.word is not None:
                self.Accumulator.add(trie_.word)
            for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                i_, j_ = di+i, dj+j
                if 0 <= i_ < len(board) and 0 <= j_ < len(board[0]):
                    if not (i_, j_) in visited:
                        self.dfs(board, i_, j_, visited, trie_)
        visited.remove((i, j))

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

# words = ["aaa"]
# board = [
#     ["a", "a"]
# ]

# words = ["a"]
# board = [
#     ["a"]
# ]

# words = ["acdb"]
# board = [
#     ["a","b"],
#     ["c","d"]
# ]

s = Solution()
print(s.findWords(board, words))
