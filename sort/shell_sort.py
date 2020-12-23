def shell_sort(data):
    # se inicia con un intervalo grande
    n = len(data)
    gap = n//2

    # se realiza una insercion con el intervalo especificado
    while gap > 0:
        for i in range(gap, n):
            temp = data[i]
            j = i
            while j >= gap and data[j-gap] > temp:
                data[j] = data[j-gap]
                j -= gap
            data[j] = temp
        gap //= 2
"""
    def shell_sort(data):
    sublist_count = len(data) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(data, start_position, sublist_count)

        print("Despues de incrementos de tamanno:", sublist_count, "la lista es:", data)

        sublist_count = sublist_count // 2


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i

        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap

        a_list[position] = current_value

"""
