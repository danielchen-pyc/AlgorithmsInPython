def binary_iter(target, list):
    start = 0
    stop = len(list) - 1
    while start <= stop:
        mid = (start + stop)//2
        if target == list[mid]:
            return f"{target} found at index {mid}"
        elif target > list[mid]:
            start = mid + 1
        else:
            stop = mid - 1
    return f"{target} not found in list"


def binary_recur(target, list, start, stop):
    if start > stop:
        return f"{target} not found in list"
    else:
        mid = (start + stop)//2
        if target == list[mid]:
            return f"{target} found at index {mid}"
        elif target > list[mid]:
            return binary_recur(target, list, mid + 1, stop)
        else:
            return binary_recur(target, list, start, mid - 1)


list = [4, 6, 2, 7, 3, 8, 3, 1, 11, 5, 9, 2]
print(binary_recur(9, sorted(list), 0, len(list) - 1))
