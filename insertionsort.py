def InsertionSort(list):
    pivot = 1
    while pivot < len(list):
        if list[pivot] < list[pivot - 1]:
            index = pivot
            swap = True
            while index > 0 and swap:
                swap = False
                if list[index] < list[index - 1]:
                    list[index - 1], list[index] = list[index], list[index - 1]
                    swap = True
                index -= 1
        pivot += 1


list = [4, 6, 2, 7, 3, 8, 3, 1, 11, 5, 9, 2]
InsertionSort(list)
print(list)
