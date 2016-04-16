# Copyright 2015 Egor Tensin <Egor.Tensin@gmail.com>
# This file is licensed under the terms of the MIT License.
# See LICENSE.txt for details.

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

if __name__ == '__main__':
    import sys
    print(merge_sort(list(map(int, sys.argv[1:]))))
else:
    from algorithms.algorithm import SortingAlgorithm
    _ALGORITHMS = [
        SortingAlgorithm('merge_sort', 'Merge sort', merge_sort),
    ]
