from sort.sort_util import less
from sort.sort_util import swap


def bubble_sort(data):
    # recorre todos los elementos de la lista
    for i in range(len(data) - 1, 0, -1):
        # los ultimos i elementos se supone que ya estan ordenados
        for j in range(i):
            # se recorre la lista desde 0 hasta len - i - 1
            # y se intercambian si el elemento anterior es mayor
            # que el siguiente
            if less(data[j+1],data[j]):
                swap(data, j+1, j)
