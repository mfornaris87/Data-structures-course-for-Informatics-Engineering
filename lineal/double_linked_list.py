from lineal.empty_exception import Empty


class DoubleLinkedList:
    """
        Definicion de la clase Lista doblemente enlazada, que utiliza la definicion de la clase Nodo doblemente enlazado
        representada internamente, que posee tres atributos: el elemento contenido, una referencia al nodo anterior y
        una referencia al nodo siguiente.
    """

    # ----------------Clase nodo doblemente enlazado-----------------------------
    class _Node:
        __slots__ = '_item', '_prev', '_next'

        def __init__(self, item, prev, next):
            self._item = item
            self._prev = prev
            self._next = next

        def get_item(self):
            return self._item

        def get_prev(self):
            return self._prev

        def get_next(self):
            return self._next

        def set_item(self, item):
            self._item = item

        def set_prev(self, prev):
            self._prev = prev

        def set_next(self, next):
            self._next = next
    # ---------------------------------------------------------------

    def __init__(self):
        """
            Constructor de la lista que inicializa las referencias a la cabeza, cola como vacios y cantidad de elementos
            de la lista en 0
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
        count = 0
        found = False
        while current is not None and not found:
            if current.get_item() is element:
                found = True
                return count
            else:
                current = current.get_next()
            count += 1
        if not found:
            raise Empty('Elemento no encontrado')

    def node_at(self, index):
        """
            Devuelve el nodo que esta en la posicion que se le pasa por parametros
        """
        if 0 >= index >= self._size:
            raise IndexError('Index Out of Bound!')
        if index == 0:
            return self._head
        else:
            current = self._head
            for i in range(index):
                current = current.get_next()
            return current

    def add(self, element: object) -> object:
        """
            Inserta un elemento al final de la lista
        """
        node = self._Node(element, None, None)
        if self._head is None:
            self._head = node
            self._tail = self._head
        else:
            self._tail.set_next(node)
            node.set_prev(self._tail)
            self._tail = node
        self._size = self._size + 1

    def add_at(self, index, element):
        """
            Inserta un elemento en el indice que se le pasa por parametros
        """
        node = self._Node(element, None, None)
        if 0 >= index >= self._size:
            raise IndexError('Index Out of Bounds!')
        if index == 0:
            node.set_next(self._head)
            self._head.set_prev(node)
            self._head = node
        elif index == self._size - 1:
            node.set_prev(self._tail)
            self._tail.set_next(node)
            self._tail = node
        else:
            prev = self.node_at(index - 1)
            next_value = self.node_at(index)
            prev.set_next(node)
            node.set_prev(prev)
            node.set_next(next_value)
            next_value.set_prev(node)
        self._size = self._size + 1

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

        found = False
        prev = None
        if self._head.get_item() is element:
            self._head = self._head.get_next()
            self._head.set_prev(None)
            found = True
        elif self._tail.get_item() is element:
            self._tail = self._tail.get_prev()
            self._tail.set_next(None)
            found = True
        else:
            current = self._head
            while not found and current is not None:
                if current.get_item() is not element:
                    prev = current
                    current = current.get_next()
                else:
                    found = True
                    prev.set_next(current.get_next())
                    current.get_next().set_prev(prev)

        if not found:
           print("Elemento no encontrado")
        else:
            self._size = self._size - 1

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
        print("[", ', '.join(str(v.get_item()) for v in self), "]")
