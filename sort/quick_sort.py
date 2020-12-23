from sort.sort_util import swap
from sort.sort_util import less


def quick_sort(list, low, high):
    # caso base, hay 0 o 1 elemento, por tanto la lista esta ordenada
    if low >= high: return
    # se selecciona como pivote el ultimo elemento de la lista
    pivot = list[high]
    # esta variable permite escanear la lista hacia la derecha
    left = low
    # esta variable permite escanear la lista hacia la izquierda
    right = high - 1
    # mientras no llegue al final de la lista
    while left <= right:
        # buscar hasta encontrar un valor igual o mayor que el pivote
        while left <= right and list[left] < pivot:
            left += 1
        # buscar hasta encontrar un valor igual o menor que el pivote
        while left <= right and pivot < list[right]:
            right -= 1
        # cuando las busquedas no coinciden directamente
        if left <= right:
            # intercambiar los valores
            list[left], list[right] = list[right], list[left]
            # disminuir el intervalo de busqueda
            left, right = left + 1, right - 1

    # poner el pivote en el lugar que le toca
    list[left], list[high] = list[high], list[left]
    quick_sort(list, low, left - 1)
    quick_sort(list, left + 1, high)
