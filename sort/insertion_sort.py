from sort.sort_util import less
from sort.sort_util import swap


def insertion_sort(data):
    """
        El primer ciclo recorre todos los elementos de la lista,
        el segundo revisa desde la primera posicion no ordenada
        hacia adelante y se intercambia el elemento cuando se
        encuentre una posicion en donde el elemento anterior
        sea menor al que se esta trabjando o sea la posicion 0
        de la lista

    :param data:
    :return:
    """
    [swap(data, j, j -1) for i in range(0, len(data)) for j in range(i, 0, -1) if less(data[j], data[j - 1])]