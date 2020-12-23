from collections import deque


class BinarySearchTree:

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

    def search(self, element):
        s = None
        if element == self._root:
            s = self
        elif int(element) < int(self._root) and not self._left.is_empty():
            s = self._left.search(element)
        elif int(element) > int(self._root) and not self._right.is_empty():
            s = self._right.search(element)
        return s

    def is_empty(self):
        return self._root is None

    def is_leaf(self):
        return self._left is None and self._right is None

    def add(self, element):
        added = False
        if self._root is None:
            self._root = element
            added = True
            return added
        else:
            if int(element) < int(self._root) and self._left is None:
                self.left = BinarySearchTree(element)
                added = True
            elif int(element) < int(self._root) and self._left is not None:
                added = self.left.add(element)
            if int(element) > int(self._root) and self._right is None:
                self.right = BinarySearchTree(element)
                added = True
            elif int(element) > int(self._root) and self._right is not None:
                added = self.right.add(element)
        return added

    def search_min(self):
        if self._root is None:
            return None
        elif self.left is None and self._right is None:
            return self._root
        elif self._left is not None:
            return self._left.search_min()

    def delete(self, element):
        delete_this = self.search(element)
        if delete_this is not None:
            if delete_this.is_leaf():
                delete_this.root = None
            else:
                if delete_this.left is not None and delete_this.right is not None:
                    aux = delete_this.right.search_min()
                    self.delete(aux)
                    delete_this.root = aux
                else:
                    if delete_this.left is not None:
                        aux = delete_this.left.root
                        self.delete(aux)
                        delete_this.root = aux
                    else:
                        aux = delete_this.right.root
                        self.delete(aux)
                        delete_this.root = aux

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