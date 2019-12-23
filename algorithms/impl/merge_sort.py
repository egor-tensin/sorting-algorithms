# Copyright (c) 2015 Egor Tensin <Egor.Tensin@gmail.com>
# This file is part of the "Sorting algorithms" project.
# For details, see https://github.com/egor-tensin/sorting-algorithms.
# Distributed under the MIT License.

import sys

from ..algorithm import SortingAlgorithm


def merge(left, right):
    result = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    if left:
        result.extend(left[l:])
    if right:
        result.extend(right[r:])
    return result


def merge_sort(xs):
    if len(xs) < 2:
        return xs
    mid = len(xs) // 2
    return merge(merge_sort(xs[:mid]), merge_sort(xs[mid:]))


_ALGORITHMS = [
    SortingAlgorithm('merge_sort', 'Merge sort', merge_sort),
]


def _parse_args(args=None):
    if args is None:
        args = sys.argv[1:]
    return list(map(int, args))


def main(args=None):
    xs = _parse_args(args)
    print(merge_sort(list(xs)))


if __name__ == '__main__':
    main()
