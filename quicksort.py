def QuickSort(list):
    if len(list) == 0 or len(list) == 1:
        return list
    else:
        pivot = list[-1]
        smaller, equal, greater = [], [], []
        equal.append(pivot)
        for index in range(len(list) - 1):
            current_num = list[index]
            if current_num > pivot:
                greater.append(current_num)
            elif current_num < pivot:
                smaller.append(current_num)
            else:
                equal.append(current_num)
        print(smaller, equal, greater)
    return QuickSort(smaller) + equal + QuickSort(greater)


list = [4, 6, 2, 7, 3, 8, 3, 1, 11, 5, 9, 2]
print(QuickSort(list))
