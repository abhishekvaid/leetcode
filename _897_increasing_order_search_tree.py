# Definition for a binary tree node.
import json


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        else:
            root.right = self.increasingBST(root.right)
            leftSideIncreasingBSTRoot = self.increasingBST(root.left)
            if leftSideIncreasingBSTRoot:
                tail = leftSideIncreasingBSTRoot
                while tail.right:
                    tail = tail.right
                tail.right = root
                root.left = None
                root = leftSideIncreasingBSTRoot
            root.left = None
            return root


root = TreeNode(5)
root.left = TreeNode(4)

s = Solution().increasingBST(root)
print(json.dumps(s))