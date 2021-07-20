def insertion_sort(list, type='iterative'):
    if(type == 'iterative'):
        insertion_sort_i(list)
    else:
        insertion_sort_r(list)


def insertion_sort_i(list):
    for i in range(len(list)):
        current = i
        previous = i - 1
        while(previous >= 0 and list[current] < list[previous]):
            list[current], list[previous] = list[previous], list[current]
            current -= 1
            previous -= 1
    return list


def insertion_sort_r(list):
    if(len(list) <= 1):
        return list
    list[:len(list)-1] = insertion_sort_r(list[:len(list)-1])
    current = len(list) - 1
    previous = current - 1
    while(previous >= 0 and list[current] < list[previous]):
        list[current], list[previous] = list[previous], list[current]
        current -= 1
        previous -= 1
    return list
