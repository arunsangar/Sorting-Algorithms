import random
import sys


def get_list(filename):
    list = []
    with open(filename) as f:
        for line in f:
            for x in line.split():
                list.append(int(x))
    return list


def get_random_list(length, min=-sys.maxsize-1, max=sys.maxsize):
    return [get_random_number(min, max) for _ in range(length)]


def get_random_number(min, max):
    return random.randint(min, max)
