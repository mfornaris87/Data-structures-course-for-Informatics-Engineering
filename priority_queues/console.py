from priority_queues.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue


if __name__ == '__main__':
    pq = AdaptableHeapPriorityQueue()
    pq.add(6, 'Maite')
    pq.add(8, 'Karel')
    pq.add(5, 'Sabrina')

    print(pq)
