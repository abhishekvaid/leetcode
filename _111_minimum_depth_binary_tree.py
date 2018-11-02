# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys


class Solution:

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            leftHeight = self.minDepth(root.left)
            rightHeight = self.minDepth(root.right)
            if not all([leftHeight, rightHeight]):
                return leftHeight + rightHeight + 1
            else:
                return min(leftHeight, rightHeight) + 1
