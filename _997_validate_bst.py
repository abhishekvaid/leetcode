# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys

class Solution:

    def _isValidBST(self, r, left, right):
        if not r:
            return True
        else:
            return all([
                left <= r.val <= right,
                self._isValidBST(r.left, left, r.val),
                self._isValidBST(r.left, r.val, right)
            ])

    def isValidBST(self, r):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not r:
            return True
        else:
            return self._isValidBST(r, -sys.maxsize, sys.maxsize)