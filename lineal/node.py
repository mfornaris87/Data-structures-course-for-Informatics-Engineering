class Node:
    __slots__ = '_item', '_next'

    def __init__(self, item):
        self._item = item
        self._next = None

    def get_item(self):
        return self._item

    def get_next(self):
        return self._next

    def set_item(self, item):
        self._item = item

    def set_next(self, next):
        self._next = next

