def less(x, y):
    if x < y: return True
    else: return False


def swap(data, i, j):
    aux = data[i]
    data[i] = data[j]
    data[j] = aux


def show(data):
    for value in data:
        print(value, " ")
    print()


def isSorted(data):
    sorted = False
    for i in range(0, len(data) - 1):
        sorted = less(data[i+1], data[i])
    return sorted

data = [1,2,3,5,4]
print(isSorted(data))