from sort.sort_util import less
from sort.sort_util import swap


def selection_sort(data):
    # recorre todos los elementos de la lista
    for i in range(0, len(data)):
        # encuentra el minimo elemento
        # en la lista restante desordenada
        min_pos = i
        for j in range(i + 1, len(data)):
            if less(data[j], data[min_pos]):
                min_pos = j
        # intercambia el minimo elemento con el de
        # la primera posicion no ordenada que se encuentre
        swap(data, i, min_pos)
