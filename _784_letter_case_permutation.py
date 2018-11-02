import string

class Solution:

    def __init__(self):
        self.Acc = []

    def letterCasePermutationRecursive(self, S, i):
        if len(S) == i:
            self.Acc.append(list(S))
        else:
            if not S[i].isdigit():
                S[i] = S[i].upper()
                self.letterCasePermutationRecursive(S, i+1)
                S[i] = S[i].lower()
                self.letterCasePermutationRecursive(S, i+1)
            else:
                self.letterCasePermutationRecursive(S, i+1)

    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        self.letterCasePermutationRecursive(list(S), 0)
        return ["".join(l) for l in self.Acc]


s = Solution().letterCasePermutation("a1b2")
print(s)