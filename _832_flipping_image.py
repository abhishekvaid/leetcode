class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # Horizontal Flip
        A = [a[::-1] for a in A]
        A = [
            [elem ^ 1 for elem in row]
            for row in A
        ]
        return A