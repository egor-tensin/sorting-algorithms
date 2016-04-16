# Copyright 2015 Egor Tensin <Egor.Tensin@gmail.com>
# This file is licensed under the terms of the MIT License.
# See LICENSE.txt for details.

def insertion_sort(xs):
    for i in range(1, len(xs)):
        j = i
        while j > 0 and xs[j - 1] > xs[j]:
            xs[j], xs[j - 1] = xs[j - 1], xs[j]
            j -= 1
    return xs

if __name__ == '__main__':
    import sys
    print(insertion_sort(list(map(int, sys.argv[1:]))))
else:
    from algorithms.algorithm import SortingAlgorithm
    _ALGORITHMS = [
        SortingAlgorithm('insertion_sort', 'Insertion sort', insertion_sort),
    ]
