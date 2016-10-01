# Copyright (c) 2016 Egor Tensin <Egor.Tensin@gmail.com>
# This file is part of the "Sorting algorithms" project.
# For details, see https://github.com/egor-tensin/sorting-algorithms.
# Distributed under the MIT License.

from heapq import heappush, heappop
import sys

from ..algorithm import Algorithm
from .quicksort import quicksort_random

def calc_median_heaps(xs):
    cur_median = 0.0
    min_heap, max_heap = [], []
    for x in xs:
        if x < cur_median:
            heappush(max_heap, -x)
        elif x > cur_median or len(max_heap) > len(min_heap):
            heappush(min_heap, x)
        else:
            heappush(max_heap, -x)

        if len(max_heap) > len(min_heap) + 1:
            heappush(min_heap, -heappop(max_heap))
        elif len(min_heap) > len(max_heap) + 1:
            heappush(max_heap, -heappop(min_heap))

        if len(max_heap) > len(min_heap):
            cur_median = -max_heap[0]
        elif len(max_heap) == len(min_heap):
            cur_median = -max_heap[0] / 2 + min_heap[0] / 2
        else:
            cur_median = min_heap[0]
    return cur_median

def calc_median_sorting(xs):
    if not xs:
        return 0.0
    quicksort_random(xs)
    if len(xs) % 2:
        return xs[len(xs) // 2]
    else:
        return xs[len(xs) // 2 - 1] / 2 + xs[len(xs) // 2] / 2

_ALGORITHMS = [
    Algorithm('median_sorting', 'Median value (using explicit sorting)', calc_median_sorting),
    Algorithm('median_heaps', 'Median value (using heaps)', calc_median_heaps),
]

def _parse_args(args=sys.argv):
    return list(map(int, args[1:]))

def main(args=sys.argv):
    xs = _parse_args(args)
    print(calc_median_sorting(list(xs)))
    print(calc_median_heaps(list(xs)))

if __name__ == '__main__':
    main()
