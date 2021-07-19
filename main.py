from SortingAlgorithms.selection_sort import selection_sort
from Utilities.helper import *

if __name__ == '__main__':
    list = get_random_list(100, 0, 100)

    new_list = selection_sort(list)

    print(new_list)
