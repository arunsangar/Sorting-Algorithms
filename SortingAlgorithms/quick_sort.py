def quick_sort(list, type='iterative'):
    if(type == 'iterative'):
        quick_sort_i(list)
    else:
        quick_sort_r(list)


def quick_sort_i(list):
    left = 0
    right = len(list)
    stack = []
    stack.append((left, right))
    while(len(stack) > 0):
        left, right = stack.pop()
        list[left:right], split = partition(list[left:right])
        split += left
        if(split > left):
            stack.append((left, split))
        if(split+1 < right):
            stack.append((split+1, right))
    return list


def quick_sort_r(list):
    if(len(list) > 1):
        list, split = partition(list)
        list[0:split] = quick_sort_r(list[0:split])
        list[split+1:len(list)] = quick_sort_r(list[split+1:len(list)])
    return list


def partition(list):
    pivot = len(list)-1
    i = 0
    for j in range(len(list)-1):
        if(list[j] <= list[pivot]):
            list[i], list[j] = list[j], list[i]
            i += 1
    list[i], list[pivot] = list[pivot], list[i]
    return list, i
