def merge(list1, list2, result):
    i = j = 0
    while i + j < len(result):
        if j == len(list2) or (i < len(list1) and list1[i] < list2[j]):
            result[i + j] = list1[i]
            i += 1
        else:
            result[i + j] = list2[j]
            j += 1


def merge_sort(data):
    n = len(data)
    # si la cantidad de elementos es menor que 2 solo devuelve, no hace nada mas
    if n < 2:
        return
    # divide
    mid = n // 2
    list1 = data[0:mid]
    list2 = data[mid:n]
    # conquista
    merge_sort(list1)
    merge_sort(list2)
    # combina
    merge(list1, list2, data)