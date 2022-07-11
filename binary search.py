from random import randint as rand
import time

def search(l, target):
    for i in range(len(l)):
        if target == l[i]:
            return i
    return -1


def binary_search(l, target, low=0, high=None):
    if high == None:
        high = len(l) - 1
    midpoint = (low + high) // 2
    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        return binary_search(l, target, midpoint+1, high)

if __name__=='__main__':
    length = int(1e4)
    l = [rand(-3*length, 3*length) for i in range(length)]
    l.sort()
    target = rand(-3*length, 3*length)

    start = time.time()
    for target in l:
        search(l, target)
    end = time.time()
    print(f"Search: {end-start}")

    start = time.time()
    for target in l:
        binary_search(l, target)
    end = time.time()
    print(f"Binary search: {end-start}")