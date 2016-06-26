# Copyright 2015 Egor Tensin <Egor.Tensin@gmail.com>
# This file is licensed under the terms of the MIT License.
# See LICENSE.txt for details.

from random import randrange, seed
import sys

from ..algorithm import SortingAlgorithm

seed()

def _partition(xs, beg, end, select_pivot):
    pivot = select_pivot(xs, beg, end)
    xs[pivot], xs[end] = xs[end], xs[pivot]
    for i in range(beg, end):
        if xs[i] <= xs[end]:
            xs[i], xs[beg] = xs[beg], xs[i]
            beg += 1
    xs[beg], xs[end] = xs[end], xs[beg]
    return beg

def _quicksort(xs, beg, end, select_pivot):
    if beg < end:
        pivot = _partition(xs, beg, end, select_pivot)
        _quicksort(xs, beg, pivot - 1, select_pivot)
        _quicksort(xs, pivot + 1, end, select_pivot)

def _select_first(xs, beg, end):
    return beg

def _select_second(xs, beg, end):
    return beg + 1

def _select_middle(xs, beg, end):
    return (beg + end) // 2

def _select_last(xs, beg, end):
    return end

def _select_random(xs, beg, end):
    return randrange(beg, end + 1)

def quicksort_first(xs):
    _quicksort(xs, 0, len(xs) - 1, _select_first)
    return xs

def quicksort_second(xs):
    _quicksort(xs, 0, len(xs) - 1, _select_second)
    return xs

def quicksort_middle(xs):
    _quicksort(xs, 0, len(xs) - 1, _select_middle)
    return xs

def quicksort_last(xs):
    _quicksort(xs, 0, len(xs) - 1, _select_last)
    return xs

def quicksort_random(xs):
    _quicksort(xs, 0, len(xs) - 1, _select_random)
    return xs

_ALGORITHMS = [
    SortingAlgorithm('quicksort_first', 'Quicksort (first element as pivot)', quicksort_first),
    SortingAlgorithm('quicksort_second', 'Quicksort (second element as pivot)', quicksort_second),
    SortingAlgorithm('quicksort_middle', 'Quicksort (middle element as pivot)', quicksort_middle),
    SortingAlgorithm('quicksort_last', 'Quicksort (last element as pivot)', quicksort_last),
    SortingAlgorithm('quicksort_random', 'Quicksort (random element as pivot)', quicksort_random),
]

def _parse_args(args=sys.argv):
    return list(map(int, args[1:]))

def main(args=sys.argv):
    xs = _parse_args(args)
    print(quicksort_first(list(xs)))
    print(quicksort_second(list(xs)))
    print(quicksort_middle(list(xs)))
    print(quicksort_last(list(xs)))
    print(quicksort_random(list(xs)))

if __name__ == '__main__':
    main()
