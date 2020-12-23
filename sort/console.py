from sort.bubble_sort import bubble_sort
from sort.selection_sort import selection_sort
from sort.insertion_sort import insertion_sort
from sort.merge_sort import merge_sort
from sort.quick_sort import quick_sort
from sort.shell_sort import shell_sort


data = [2, 3, 1, 9, 6, 4, 5, 7, 8]
print("Lista original:", data)
bubble_sort(data)
print("Ordenado con burbuja clasica", data)

data = [2, 3, 1, 9, 6, 4, 5, 7, 8]
selection_sort(data)
print("Ordenado con selection sort:", data)

data = [2, 3, 1, 9, 6, 4, 5, 7, 8]
insertion_sort(data)
print("Ordenado con insertion sort:", data)

data = [2, 3, 1, 9, 6, 4, 5, 7, 8]
merge_sort(data)
print("Ordenado con MergeSort:", data)

data = [2, 3, 1, 9, 6, 4, 5, 7, 8]
quick_sort(data, 0, len(data)-1)
print("Ordenando con Quicksort:", data)

data = [2, 3, 1, 9, 6, 4, 5, 7, 8]
shell_sort(data)
print("Ordenando con Shellsort:", data)



