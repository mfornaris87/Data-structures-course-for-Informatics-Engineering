from collections import deque


class BinaryTree:

    def __init__(self, element=None):
        self._root = element
        self._left = None
        self._right = None

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, value):
        self._root = value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self._left = value

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        self._right = value

    def add_left(self, child):
        added = False
        if self._left is None:
            self._left = BinaryTree(child)
            added = True
        else:
            bt = BinaryTree(child)
            bt._left = self._left
            self._left = bt
            added = True
        return added

    def add_right(self, child):
        added = False
        if self._right is None:
            self.right = BinaryTree(child)
            added = True
        else:
            bt = BinaryTree(child)
            bt._right = self._right
            self._right = bt
            added = True
        return added

    def add_child(self, parent, child):
        added = False
        if parent is None and self._root is None:
            self._root = child
            added = True
        if self._root == parent and self._left is None:
            added = self.add_left(child)
        elif self._root == parent and self._right is None:
            added = self.add_right(child)
            return True
        if added is False and self._left is not None:
            added = self._left.add_child(parent, child)
        if added is False and self._right is not None:
            added = self._right.add_child(parent, child)
        return added

    def search(self, element):
        return

    def is_leaf(self):
        return self._left is None and self._right is None

    def is_empty(self):
        return self._root is None

    def height(self):
        return

    def preorder(self):
        pre = []
        pre.append(self._root)
        if self._left is not None:
            pre.append(self._left.preorder())
        if self._right is not None:
            pre.append(self._right.preorder())
        return pre

    def postorder(self):
        post = []
        if self._left is not None:
            post.append(self._left.postorder())
        if self._right is not None:
            post.append(self._right.postorder())
        post.append(self._root)
        return post

    def inorder(self):
        ino = []
        if self.is_leaf():
            ino.append(self._root)
        else:
            if self._left is not None:
                ino.append(self._left.inorder())
            ino.append(self._root)
            if self._right is not None:
                ino.append(self._right.inorder())
        return ino

    def bfs(self):
        wide = []
        queue = deque()
        queue.append(self)
        while len(queue) != 0:
            wide.append(queue[0].root)
            if queue[0].left is not None:
                queue.append(queue[0].left)
            if queue[0].right is not None:
                queue.append(queue[0].right)
            queue.popleft()
        return wide

    def print_tree(self):
            print("[", ', '.join(str(value) for value in self.bfs()), "]")
