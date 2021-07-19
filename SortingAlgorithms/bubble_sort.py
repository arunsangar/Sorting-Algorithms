def bubble_sort(list, type='iterative'):
    if(type == 'iterative'):
        bubble_sort_i(list)
    else:
        bubble_sort_r(list)


def bubble_sort_i(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if(list[j] > list[j+1]):
                list[j], list[j+1] = list[j+1], list[j]
    return list


def bubble_sort_r(list):
    if(len(list) <= 1):
        return list
    for i in range(len(list)-1):
        if(list[i] > list[i+1]):
            list[i], list[i+1] = list[i+1], list[i]
    list[:len(list)-1] = bubble_sort_r(list[:len(list)-1])
    return list
