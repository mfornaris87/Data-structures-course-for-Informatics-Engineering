def binary_search(a_list, element):
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and found == False:
        mid = (first + last) // 2
        if a_list[mid] == element:
            found = True
        elif element < a_list[mid]:
            last = mid - 1
        else:
            first = mid + 1

    return found

