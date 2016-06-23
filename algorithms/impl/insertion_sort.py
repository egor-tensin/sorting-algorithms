# Copyright 2015 Egor Tensin <Egor.Tensin@gmail.com>
# This file is licensed under the terms of the MIT License.
# See LICENSE.txt for details.

import sys

from ..algorithm import SortingAlgorithm

def insertion_sort(xs):
    for i in range(1, len(xs)):
        j = i
        while j > 0 and xs[j - 1] > xs[j]:
            xs[j], xs[j - 1] = xs[j - 1], xs[j]
            j -= 1
    return xs

_ALGORITHMS = [
    SortingAlgorithm('insertion_sort', 'Insertion sort', insertion_sort),
]

def _parse_args(args=sys.argv):
    return list(map(int, args[1:]))

def main(args=sys.argv):
    xs = _parse_args(args)
    print(insertion_sort(list(xs)))

if __name__ == '__main__':
    main()
