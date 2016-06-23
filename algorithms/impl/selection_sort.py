# Copyright 2015 Egor Tensin <Egor.Tensin@gmail.com>
# This file is licensed under the terms of the MIT License.
# See LICENSE.txt for details.

import sys

from ..algorithm import SortingAlgorithm

def selection_sort(xs):
    for i in range(len(xs) - 1):
        min_i = i
        for j in range(i + 1, len(xs)):
            if xs[j] < xs[min_i]:
                min_i = j
        if min_i != i:
            xs[i], xs[min_i] = xs[min_i], xs[i]
    return xs

_ALGORITHMS = [
    SortingAlgorithm('selection_sort', 'Selection sort', selection_sort),
]

def _parse_args(args=sys.argv):
    return list(map(int, args[1:]))

def main(args=sys.argv):
    xs = _parse_args(args)
    print(selection_sort(list(xs)))

if __name__ == '__main__':
    main()
