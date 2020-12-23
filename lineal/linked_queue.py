from lineal.node import Node
from lineal.empty_exception import Empty


class LinkedQueue:
    """
        Implementacion de la cola mediante nodos simplemente enlazados
    """

    def __init__(self):
        """
           Constructor de la clase que inicializa las referencias a la cabeza y cola del TDA vacios y la cantidad de
           elementos en 0
        """
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """
            Devuevle la cantidad de elementos de la lista
        :return:
        """
        return self._size

    def is_empty(self):
        """
            Devuelve verdadero si la lista esta vacia
        :return:
        """
        return self._size == 0

    def peek(self):
        """
            Devuelve el primer elemento de la cola, pero no lo elimina
        :return:
        """
        if self.is_empty():
            return 'The Queue is empty!'
        return self._head.get_item()

    def dequeue(self):
        """
           Devuelve y elimina el primer elemento de la cola
        :return:
        """
        if self.is_empty():
            raise Empty('La cola esta vacia')
        element = self.peek()
        self._head = self._head.get_next()
        self._size -= 1
        return element

    def enqueue(self, element):
        """
            Encola un nuevo elemento al final de la cola
        :param element:
        :return:
        """
        node = Node(element)
        if self.is_empty():
            self._head = node
        else:
            self._tail.set_next(node)
        self._tail = node
        self._size += 1

    def print_queue(self):
        """
           Imprime la cola por consola
        :return:
        """
        q = []
        while not self.is_empty():
            q.append(self.dequeue())
        for v in q:
            self.enqueue(v)
        print("[", ', '.join(str(value) for value in q), "]")