from lineal.node import Node
from lineal.empty_exception import Empty


class LinkedList:
    """
        Definicion de la estructura de datos lista simplemente enlazada, basada en nodos que contiene solo el elemento
        y una referencia al nodo siguiente
    """

    def __init__(self):
        """
            Constructor de la clase que inicializa las referencias a la cabeza y cola de la lista vacias y la cantidad
            de elementos de la lista en 0
        """
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """
            Devuelve la cantidad de elementos en la lista
        """
        return self._size

    def index_of(self, element):
        """
            Devuelve el indice del elemento que se le pasa por parametros
        """
        current = self._head
        found = False
        count = 0
        while current is not None and not found:
            if current.get_item() == element:
                found = True
                return count
            else:
                current = current.get_next()
            count += 1

    def node_at(self, index):
        """
            Devuelve el nodo que esta en la posicion que se le pasa por parametros
        """
        if 0 >= index >= self._size:
            raise IndexError('Index Out of Bounds!')
        if index == 0:
            return self._head
        else:
            node = self._head
            for i in range(index):
                node = node.get_next()
            return node

    def add(self, element: object) -> object:
        """
            Inserta un elemento al final de la lista
        """
        new_node = Node(element)
        if self._head is None:
            self._head = new_node
            self._tail = self._head
        else:
            self._tail.set_next(new_node)
            self._tail = new_node
        self._size += 1

    def add_at(self, index, element):
        """
            Inserta un elemento en el indice que se le pasa por parametros
        """
        node = Node(element)
        if 0 >= index >= self._size:
            raise IndexError('Index Out of Bounds!')
        if index == 0:
            node.set_next(self._head)
            self._head = node
        elif index == self._size - 1:
            self._tail.set_next(node)
            self._tail = node
        else:
            prev = self.node_at(index - 1)
            next = self.node_at(index)
            prev.set_next(node)
            node.set_next(next)
        self._size += 1

    def add_collection(self, new_list):
        """
            Inserta todos los elementos de la lista que se le pasa por parametros
        """
        for value in new_list:
            self.add(value)

    def remove(self, element):
        """
            Elimina el elemento que se le pasa por parametros
        """
        current = self._head
        prev = None
        found = False
        while not found and current is not None:
            if current.get_item() is element:
                found = True
            else:
                prev = current
                current = current.get_next()
        if prev is None:
            self._head = current.get_next()
        else:
            prev.set_next(current.get_next())
        self._size -= 1
        self._tail = self.node_at(self._size - 1)
        if not found:
            print('Elemento no encontrado')

    def __iter__(self):
        """
            Convierte la lista en un objeto iterable
        """
        current = self._head
        while current is not None:
            yield current
            current = current.get_next()

    def print_list(self):
        """
            Imprime la lista en un formato elegante
        """
        print("[", ', '.join(str(value.get_item()) for value in self), "]")

