# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def generateCounts(self, root):
        if not root:
            return 0
        else:
            root.counts = [self.generateCounts(root.left), self.generateCounts(root.right)]
            return 1 + sum(root.counts)

    def _recursiveKthSmallest(self, root, k):
        leftCount, rightCount = root.counts
        if k == leftCount + 1:
            return root.val
        elif k <= leftCount:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k - (leftCount+1))

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.generateCounts(root)
        return self._recursiveKthSmallest(root, k)
