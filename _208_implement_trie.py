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


T = Trie()
T.insert("Abhishek")
assert T.startsWith("") == True
assert T.startsWith("Abhis") == True
assert T.startsWith("Abhi") == True
assert T.startsWith("Abhin") == False
T.insert("Abhiraj")
assert T.startsWith("Abhi") == True
assert T.search("Abhilasha") == False
assert T.search("Abhishek") == True
assert T.search("Abhirag") == False
assert T.search("Abhiraj") == True
T.insert("Kanav")
assert T.startsWith("K") == True
assert T.startsWith("Kana") == True
assert T.search("Kana") == False
assert T.search("Kanav") == True

assert T.search("Abhishekv") == False
