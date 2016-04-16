# Copyright 2015 Egor Tensin <Egor.Tensin@gmail.com>
# This file is licensed under the terms of the MIT License.
# See LICENSE.txt for details.

def selection_sort(xs):
    for i in range(len(xs) - 1):
        min_i = i
        for j in range(i + 1, len(xs)):
            if xs[j] < xs[min_i]:
                min_i = j
        if min_i != i:
            xs[i], xs[min_i] = xs[min_i], xs[i]
    return xs

if __name__ == '__main__':
    import sys
    print(selection_sort(list(map(int, sys.argv[1:]))))
else:
    from algorithms.algorithm import SortingAlgorithm
    _ALGORITHMS = [
        SortingAlgorithm('selection', 'Selection sort', selection_sort),
    ]
