# Copyright 2015 Egor Tensin <Egor.Tensin@gmail.com>
# This file is licensed under the terms of the MIT License.
# See LICENSE.txt for details.

def bubble_sort(xs):
    while True:
        swapped = False
        for i in range(1, len(xs)):
            if xs[i - 1] > xs[i]:
                xs[i], xs[i - 1] = xs[i - 1], xs[i]
                swapped = True
        if not swapped:
            break
    return xs

def bubble_sort_optimized(xs):
    n  = len(xs)
    while True:
        new_n = 0
        for i in range(1, n):
            if xs[i - 1] > xs[i]:
                xs[i], xs[i - 1] = xs[i - 1], xs[i]
                new_n = i
        n = new_n
        if not n:
            break
    return xs

if __name__ == '__main__':
    import sys
    xs = list(map(int, sys.argv[1:]))
    print(bubble_sort(list(xs)))
    print(bubble_sort_optimized(list(xs)))
else:
    from algorithms.algorithm import SortingAlgorithm
    _ALGORITHMS = [
        SortingAlgorithm('bubble_sort', 'Bubble sort', bubble_sort),
        SortingAlgorithm('bubble_sort_optimized', 'Bubble sort (optimized)', bubble_sort_optimized),
    ]
