# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import queue


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        Q, Q_ = queue.Queue(), queue.Queue()
        if root:
            Q.put(root)
        Acc = []
        while not Q.empty() and Q_.empty():
            Acc.append([])
            while not Q.empty():
                ele = Q.get()
                Acc[-1].append(ele.val)
                if ele.left:
                    Q_.put(ele.left)
                if ele.right:
                    Q_.put(ele.right)
            Q, Q_ = Q_, Q
        return Acc
