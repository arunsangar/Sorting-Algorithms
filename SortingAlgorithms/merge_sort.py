def merge_sort(list, type='iterative'):
    if(type == 'iterative'):
        merge_sort_i(list)
    else:
        merge_sort_r(list)


def merge_sort_i(list):
    block = 1
    length = len(list) - 1
    while(block <= length):
        for i in range(0, length, 2*block):
            left = i
            middle = i + block
            right = min(i+2*block-1, length) + 1
            list[left:right] = merge(list[left:middle], list[middle:right])
        block = 2*block
    return list


def merge_sort_r(list):
    if(len(list) > 1):
        middle = len(list)//2
        left = merge_sort_r(list[:middle])
        right = merge_sort_r(list[middle:])
        list[:] = merge(left, right)
    return list


def merge(left, right):
    i = j = k = 0
    list = []
    while(i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            list.append(left[i])
            i += 1
        else:
            list.append(right[j])
            j += 1
    while(i < len(left)):
        list.append(left[i])
        i += 1
    while(j < len(right)):
        list.append(right[j])
        j += 1
    return list
