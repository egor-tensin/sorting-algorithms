# Copyright (c) 2015 Egor Tensin <Egor.Tensin@gmail.com>
# This file is part of the "Sorting algorithms" project.
# For details, see https://github.com/egor-tensin/sorting-algorithms.
# Distributed under the MIT License.

import sys

from ..algorithm import SortingAlgorithm

# Disclaimer: implemented in the most literate way.


def heapsort(xs):
    _heapify(xs)
    first, last = 0, len(xs) - 1
    for end in range(last, first, -1):
        xs[end], xs[first] = xs[first], xs[end]
        _siftdown(xs, first, end - 1)
    return xs


# In a heap stored in a zero-based array,
# left_child = node * 2 + 1
# right_child = node * 2 + 2
# parent = (node - 1) // 2


def _get_parent(node):
    return (node - 1) // 2


def _get_left_child(node):
    return node * 2 + 1


def _get_right_child(node):
    return node * 2 + 2


def _heapify(xs):
    last = len(xs) - 1
    first_parent, last_parent = 0, _get_parent(last)
    for parent in range(last_parent, first_parent - 1, -1):
        _siftdown(xs, parent, last)


def _siftdown(xs, start, end):
    root = start
    while True:
        # We swap if there is at least one child
        child = _get_left_child(root)
        if child > end:
            break
        # If there are two children, select the minimum
        right_child = _get_right_child(root)
        if right_child <= end and xs[child] < xs[right_child]:
            child = right_child
        if xs[root] < xs[child]:
            xs[root], xs[child] = xs[child], xs[root]
            root = child
        else:
            break


_ALGORITHMS = [
    SortingAlgorithm('heapsort', 'Heapsort', heapsort),
]


def _parse_args(args=None):
    if args is None:
        args = sys.argv[1:]
    return list(map(int, args))


def main(args=None):
    xs = _parse_args(args)
    print(heapsort(list(xs)))


if __name__ == '__main__':
    main()
