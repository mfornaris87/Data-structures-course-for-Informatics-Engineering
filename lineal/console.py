from lineal.single_linked_list import LinkedList
from lineal.double_linked_list import DoubleLinkedList
from lineal.linked_stack import LinkedStack
from lineal.linked_queue import LinkedQueue
from collections import deque


def test_single_linked_list():
    linked_list = LinkedList()
    linked_list.add_collection([12, 13, 14, 15, 16, 17])
    linked_list.print_list()

    linked_list.add_at(3, 10)
    linked_list.print_list()

    linked_list.remove(17)
    linked_list.print_list()


def test_dl_list():
    l = DoubleLinkedList()
    l.add_collection([5, 10, 15, 20, 25, 30])
    l.print_list()
    l.remove(5)
    l.print_list()


def test_linked_stack():
    s = LinkedStack()
    print("Esta vacia la pila?", s.is_empty())
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.print_stack()
    s.pop()
    s.print_stack()
    s.pop()
    s.print_stack()

    print(s.peek())
    print("Esta vacia la pila?", s.is_empty())


def test_linked_queue():
    q = LinkedQueue()
    print('Esta vacia la cola?', q.is_empty())
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print('Esta vacia la cola?', q.is_empty())
    q.print_queue()
    print(q.peek())
    q.dequeue()
    print(q.peek())
    q.print_queue()
    q.dequeue()
    q.print_queue()


if __name__ == '__main__':
    # test_array_list()
    # test_single_linked_list()
    test_dl_list()
    # test_linked_stack()
    # test_linked_queue()
    # test_array_stack()
    # test_array_queue()

    d = deque('abc')

    # funcionamiento de cola
    d.append('d')      # enqueue
    d.append('e')      # enqueue
    d.popleft()        # dequeue
    # print(d)
    # print(d[0])        # peek

    # funcionamiento de pila
    d.append('f')      # push
    d.append('g')      # push
    d.pop()            # pop
    # print(d)
    # print(d[len(d)-1]) # peek






