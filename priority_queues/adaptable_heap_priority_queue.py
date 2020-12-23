from priority_queues.heap_priority_queue import HeapPriorityQueue, Empty


class AdaptableHeapPriorityQueue(HeapPriorityQueue):

    class Locator(HeapPriorityQueue._Item):
        __slots__ = '_index'

        def __init__(self, k, v, j):
            HeapPriorityQueue.__init__(k, v)
            self._index = j

        @property
        def index(self):
            return self._index

    # ---------------Non-public behabior------------------------------------
    def _swap(self, i, j):
        HeapPriorityQueue._swap(i, j)
        self._data[i]._index = i
        self._data[j]._index = j

    def _bubble(self, j):
        if j > 0 and self.data[j] < self.data[self.parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)

    def add(self, key, value):
        token = self.Locator(key, value, len(self.data))
        self.data.append(token)
        self._upheap(len(self.data) - 1)
        return token

    def update(self, loc, newkey, newval):
        j = loc.index
        if not 0 <= j < len(self) and self.data[j] is loc:
            raise Empty('Invalid locator')
        loc.key = newkey
        loc.value = newval
        self._bubble(j)

    def remove(self, loc):
        j = loc._index
        if not 0 <= j < len(self) and self.data[j] is loc:
            raise ValueError('Invalid locator')
        if j == len(self) - 1:
            self.data.pop()
        else:
            self._swap(j, len(self)-1)
            self.data.pop()
            self._bubble(j)
        return loc.key, loc.value
