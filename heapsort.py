# Copyright 2015 Egor Tensin <Egor.Tensin@gmail.com>
# This file is licensed under the terms of the MIT License.
# See LICENSE.txt for details.

# Disclaimer: implemented in the most literate way.

def heapsort(xs):
    heapify(xs)
    first, last = 0, len(xs) - 1
    for end in range(last, first, -1):
        xs[end], xs[first] = xs[first], xs[end]
        siftdown(xs, first, end - 1)
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

def heapify(xs):
    last = len(xs) - 1
    first_parent, last_parent = 0, _get_parent(last)
    for parent in range(last_parent, first_parent - 1, -1):
        siftdown(xs, parent, last)

def siftdown(xs, start, end):
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

if __name__ == '__main__':
    import sys
    print(heapsort(list(map(int, sys.argv[1:]))))
