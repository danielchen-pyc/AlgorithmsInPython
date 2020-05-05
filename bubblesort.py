def BubbleSort(list):
    swap = False
    while not swap:
        for index in len(list) - 1:
            num1 = list[index]
            num2 = list[index + 1]
            if num2 > num1:
                list[index], list[index + 1] = num2, num1
                swap = True





list = [4, 6, 2, 7, 3, 8, 3, 1, 11, 5, 9, 2]
BubbleSort(list)
print(list)
