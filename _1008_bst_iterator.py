# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

from queue import Queue

from queue import LifoQueue

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.next = None
        self.S = LifoQueue()
        if root:
            self.S.put(root)

    def _inorder(self):
        if not self.S.empty():
            top = self.S.get()
            while top.left:
                self.S.put(top)
                top = top.left
            if top.right:
                self.S.put(top.right)
            return top

    def hasNext(self):
        """
        :rtype: bool
        """
        self.next = self._inorder()
        return True if self.next else False

    def next(self):
        """
        :rtype: int
        """
        return self.next.val

        # Your BSTIterator will be called like this:
        # i, v = BSTIterator(root), []
        # while i.hasNext(): v.append(i.next())
