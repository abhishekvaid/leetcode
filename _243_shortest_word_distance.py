from bisect import bisect_left
import sys


class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = [i for i, w in enumerate(words) if w == word1]
        l2 = [i for i, w in enumerate(words) if w == word2]
        if len(l1) > len(l2):
            l2, l1 = l1, l2
        res = sys.maxsize
        for val in l1:
            searchIndex = bisect_left(l2, val)
            if searchIndex == 0:
                res = min([res, l2[searchIndex] - val])
            elif searchIndex == len(l2):
                res = min([res, val - l2[searchIndex-1]])
            else:
                res = min([res, l2[searchIndex] - val, val - l2[searchIndex-1]])
        return res


x = Solution().shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice")
print(x)
x = Solution().shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding")
print(x)