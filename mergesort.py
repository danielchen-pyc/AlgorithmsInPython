def MergeSort(list):
    return divide_and_conquer(list)

def merge_lists(list1, list2):
    i, j = 0, 0
    result = []
    while i < len(list1) and j < len(list2):
        print(list1, list2, i, j)
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    if i == len(list1):
        result.extend(list2[j:])
    if j == len(list2):
        result.extend(list1[i:])
    return result


def divide_and_conquer(list):
    if len(list) == 1:
        return list
    else:
        return merge_lists(divide_and_conquer(list[:len(list)//2]), divide_and_conquer(list[len(list)//2:]))


list = [4, 6, 2, 7, 3, 8, 3, 1, 11, 5, 9, 2]
print(MergeSort(list))
