# Copyright 2016 Egor Tensin <Egor.Tensin@gmail.com>
# This file is licensed under the terms of the MIT License.
# See LICENSE.txt for details.

from algorithms.impl.quicksort import quicksort_random

from heapq import *

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

def calc_median_sort_first(xs):
    if not xs:
        return 0.0
    quicksort_random(xs)
    if len(xs) % 2:
        return xs[len(xs) // 2]
    else:
        return xs[len(xs) // 2 - 1] / 2 + xs[len(xs) // 2] / 2

if __name__ == '__main__':
    import sys
    xs = list(map(int, sys.argv[1:]))
    print(calc_median_sort_first(list(xs)))
    print(calc_median_heaps(list(xs)))
else:
    from algorithms.algorithm import Algorithm
    _ALGORITHMS = [
        Algorithm('median_sort_first', 'Median (input is sorted first)', calc_median_sort_first),
        Algorithm('median_heaps', 'Median (using heaps)', calc_median_heaps),
    ]
