class PriorityQueueBase:
    """Abstract base class for a priority queue"""

    class _Item:
        """Lightweight composite to store priority queue items"""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        @property
        def key(self):
            return self._key

        @property
        def value(self):
            return self._value

        def __lt__(self, other):
            """Compare items based on their keys"""
            return self._key < other.key

    def is_empty(self):
        """Return True if the prioritiy queue is empty"""
        return len(self) == 0
