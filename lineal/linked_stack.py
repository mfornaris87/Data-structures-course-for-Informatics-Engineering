from lineal.node import Node
from lineal.empty_exception import Empty


class LinkedStack:
    """
        Clase que implementa el TDA Pila mediante nodos simplemente enlazados
    """

    def __init__(self):
        """
            Constructor que inicializa la referencia al ultimo nodo insertado en la pila vacio y la cantidad de elementos
            en 0
        """
        self._top = None
        self._size = 0

    def __len__(self):
        """
            Devuelve la cantidad de elementos en la pila
        :return:
        """
        return self._size

    def is_empty(self):
        """
            Devuelve verdadero si la pila esta vacia
        :return:
        """
        return self._size == 0

    def push(self, element):
        """
            Inserta un nuevo elemento en el tope de la pila
        :param element:
        :return:
        """
        node = Node(element)
        node.set_next(self._top)
        self._top = node
        self._size = self._size + 1

    def pop(self):
        """
            Elimina y devuelve el elemento en el tope de la pila
        :return:
        """
        if self.is_empty():
            raise Empty('La pila esta vacia')
        element = self.peek()
        self._top = self._top.get_next()
        self._size = self._size - 1
        return element

    def peek(self):
        """
            Devuelve el elemento al tope de la pila, pero no lo elimina
        :return:
        """
        if self.is_empty():
            raise Empty('La pila esta vacia')
        return self._top.get_item()

    def print_stack(self):
        """
            Imprime por consola toda la pila
        :return:
        """
        s = []
        while not self.is_empty():
            s.append(self.pop())
        for i in range(len(s)-1, -1, -1):
            self.push(s[i])
        print("[", ', '.join(str(value) for value in s), "]")
