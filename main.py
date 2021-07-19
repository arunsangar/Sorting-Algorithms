from SortingAlgorithms.selection_sort import selection_sort
from SortingAlgorithms.bubble_sort import bubble_sort
from Utilities.helper import *

if __name__ == '__main__':
    # selection sort
    list = get_random_list(30, 0, 200)
    selection_sort(list)
    print(list)

    # bubble sort iterative
    list = get_random_list(30, 0, 200)
    bubble_sort(list, 'iterative')
    print(list)

    # bubble sort recursive
    list = get_random_list(30, 0, 200)
    bubble_sort(list, 'recursive')
    print(list)
