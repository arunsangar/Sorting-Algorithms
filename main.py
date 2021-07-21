from SortingAlgorithms.selection_sort import selection_sort
from SortingAlgorithms.bubble_sort import bubble_sort
from SortingAlgorithms.insertion_sort import insertion_sort
from SortingAlgorithms.merge_sort import merge_sort
from SortingAlgorithms.quick_sort import quick_sort
from SortingAlgorithms.counting_sort import counting_sort
from Utilities.helper import *

if __name__ == '__main__':
    # selection sort
    list = get_random_list(30, 0, 200)
    print('Selection Sort\nOriginal: ', list)
    selection_sort(list)
    print('Sorted:   ', list, '\n')

    # bubble sort iterative
    list = get_random_list(30, 0, 200)
    print('Bubble Sort Iterative\nOriginal: ', list)
    bubble_sort(list, 'iterative')
    print('Sorted:   ', list, '\n')

    # bubble sort recursive
    list = get_random_list(30, 0, 200)
    print('Bubble Sort Recursive\nOriginal: ', list)
    bubble_sort(list, 'recursive')
    print('Sorted:   ', list, '\n')

    # insertion sort iterative
    list = get_random_list(30, 0, 200)
    print('Insertion Sort Iterative\nOriginal: ', list)
    insertion_sort(list, 'iterative')
    print('Sorted:   ', list, '\n')

    # insertion sort recursive
    list = get_random_list(30, 0, 200)
    print('Insertion Sort Recursive\nOriginal: ', list)
    insertion_sort(list, 'recursive')
    print('Sorted:   ', list, '\n')

    # merge sort iterative
    list = get_random_list(30, 0, 200)
    print('Merge Sort Iterative\nOriginal: ', list)
    merge_sort(list, 'iterative')
    print('Sorted:   ', list, '\n')

    # merge sort recursive
    list = get_random_list(30, 0, 200)
    print('Merge Sort Recursive\nOriginal: ', list)
    merge_sort(list, 'recursive')
    print('Sorted:   ', list, '\n')

    # quick sort iterative
    list = get_random_list(30, 0, 200)
    print('Quick Sort Iterative\nOriginal: ', list)
    quick_sort(list, 'iterative')
    print('Sorted:   ', list, '\n')

    # quick sort recursive
    list = get_random_list(30, 0, 200)
    print('Quick Sort Recursive\nOriginal: ', list)
    quick_sort(list, 'recursive')
    print('Sorted:   ', list, '\n')

    # counting sort
    list = get_random_list(30, 0, 200)
    print('Counting Sort\nOriginal: ', list)
    counting_sort(list)
    print('Sorted:   ', list, '\n')
