import itertools
from copy import deepcopy
from math import floor


class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(M), len(M[0])
        M_ = deepcopy(M)
        for i in range(m):
            for j in range(n):
                neighbours = [
                    M[i+di][j+dj]
                    for di, dj in itertools.product([0, 1, -1], [0, 1, -1])
                    if 0 <= i + di < m
                    if 0 <= j + dj < n
                ]
                M_[i][j] = floor(sum(neighbours) / len(neighbours))

        return M_


M = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
]

M = [
    [2,3,4],
    [5,6,7],
    [8,9,10],
    [11,12,13],
    [14,15,16]
]

Expected = [
    [4,4,5],
    [5,6,6],
    [8,9,9],
    [11,12,12],
    [13,13,14]
]

s = Solution().imageSmoother(M)
print(s)