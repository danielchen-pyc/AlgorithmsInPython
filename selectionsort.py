def SelectionSort(list):
    pivot = 0
    while pivot < len(list):
        for index in range(pivot, len(list)):
            if list[index] < list[pivot]:
                num1 = list[pivot]
                num2 = list[index]
                list[pivot], list[index] = num2, num1
        pivot += 1





list = [4, 6, 2, 7, 3, 8, 3, 1, 11, 5, 9, 2]
SelectionSort(list)
print(list)
