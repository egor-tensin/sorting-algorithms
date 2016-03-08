# Copyright 2015 Egor Tensin <Egor.Tensin@gmail.com>
# This file is licensed under the terms of the MIT License.
# See LICENSE.txt for details.

from enum import Enum
import gc
from time import clock

class InputKind(Enum):
    SORTED, RANDOMIZED, REVERSED = 'sorted', 'randomized', 'reversed'

    def __str__(self):
        return self.value

class SortingAlgorithm(Enum):
    BUBBLE = 'bubble'
    BUBBLE_OPTIMIZED = 'bubble_optimized'
    HEAP = 'heap'
    INSERTION = 'insertion'
    MERGE = 'merge'
    QUICK_FIRST = 'quick_first'
    QUICK_SECOND = 'quick_second'
    QUICK_MIDDLE = 'quick_middle'
    QUICK_LAST = 'quick_last'
    QUICK_RANDOM = 'quick_random'
    SELECTION = 'selection'

    def __str__(self):
        return self.value

def _get_context():
    def natural_number(s):
        n = int(s)
        if n < 0:
            raise argparse.ArgumentTypeError('cannot be negative')
        return n
    def positive_number(s):
        n = int(s)
        if n < 1:
            raise argparse.ArgumentTypeError('must be positive')
        return n
    def input_kind(s):
        try:
            return InputKind(s)
        except ValueError:
            raise argparse.ArgumentError()
    def sorting_algorithm(s):
        try:
            return SortingAlgorithm(s)
        except ValueError:
            raise argparse.ArgumentError()
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--repetitions', '-r',
                        type=positive_number, default=1,
                        help='set number of sorting repetitions')
    parser.add_argument('--input', '-i',
                        choices=tuple(x for x in InputKind),
                        type=input_kind, default=InputKind.RANDOMIZED,
                        help='choose initial input state')
    parser.add_argument('--algorithm', '-l', required=True,
                        choices=tuple(x for x in SortingAlgorithm),
                        type=sorting_algorithm,
                        help='select sorting algorithm to use')
    parser.add_argument('--min', '-a', type=natural_number,
                        required=True, dest='min_input_length',
                        help='set min input length')
    parser.add_argument('--max', '-b', type=natural_number,
                        required=True, dest='max_input_length',
                        help='set max input length')
    parser.add_argument('--output', '-o', dest='plot_path',
                        help='set plot output path')
    args = parser.parse_args()
    if args.max_input_length < args.min_input_length:
        parser.error('max input length cannot be less than min input length')
    return args

def get_timestamp():
    return clock()

def init_clock():
    get_timestamp()

def gen_input(args, n):
    if args.input is InputKind.SORTED:
        return list(range(n))
    elif args.input is InputKind.REVERSED:
        return sorted(range(n), reverse=True)
    elif args.input is InputKind.RANDOMIZED:
        from random import sample
        return sample(range(n), n)
    else:
        raise NotImplementedError(
            'invalid initial input state \'{}\''.format(args.input))

def measure_running_time(ctx, algorithm, input_length):
    xs = gen_input(ctx, input_length)
    assert algorithm(list(xs)) == sorted(xs)
    input_copies = [list(xs) for i in range(ctx.repetitions)]
    gc.disable()
    starting_time = get_timestamp()
    for i in range(ctx.repetitions):
        algorithm(input_copies[i])
    running_time = get_timestamp() - starting_time
    gc.enable()
    return running_time

def _decorate_plot(ctx, plt):
    plt.grid()
    plt.xlabel('Input length')
    plt.ylabel('Running time (sec)')
    plt.title('{} sort, {} repetition(s), {} input'.format(
        ctx.algorithm, ctx.repetitions, ctx.input))

def plot_algorithm(ctx, algorithm):
    import matplotlib.pyplot as plt
    _decorate_plot(ctx, plt)
    input_length = range(ctx.min_input_length,
                         ctx.max_input_length + 1)
    running_time = []
    for n in input_length:
        running_time.append(measure_running_time(ctx, algorithm, n))
    plt.plot(input_length, running_time)
    if ctx.plot_path is not None:
        plt.savefig(ctx.plot_path)
    else:
        plt.show()

def plot(ctx):
    if ctx.algorithm is SortingAlgorithm.BUBBLE:
        from bubble_sort import bubble_sort
        plot_algorithm(ctx, bubble_sort)
    elif ctx.algorithm is SortingAlgorithm.BUBBLE_OPTIMIZED:
        from bubble_sort import bubble_sort_optimized
        plot_algorithm(ctx, bubble_sort_optimized)
    elif ctx.algorithm is SortingAlgorithm.HEAP:
        from heapsort import heapsort
        plot_algorithm(ctx, heapsort)
    elif ctx.algorithm is SortingAlgorithm.INSERTION:
        from insertion_sort import insertion_sort
        plot_algorithm(ctx, insertion_sort)
    elif ctx.algorithm is SortingAlgorithm.MERGE:
        from merge_sort import merge_sort
        plot_algorithm(ctx, merge_sort)
    elif ctx.algorithm is SortingAlgorithm.QUICK_FIRST:
        from quicksort import quicksort_first
        plot_algorithm(ctx, quicksort_first)
    elif ctx.algorithm is SortingAlgorithm.QUICK_SECOND:
        from quicksort import quicksort_second
        plot_algorithm(ctx, quicksort_second)
    elif ctx.algorithm is SortingAlgorithm.QUICK_MIDDLE:
        from quicksort import quicksort_middle
        plot_algorithm(ctx, quicksort_middle)
    elif ctx.algorithm is SortingAlgorithm.QUICK_LAST:
        from quicksort import quicksort_last
        plot_algorithm(ctx, quicksort_last)
    elif ctx.algorithm is SortingAlgorithm.QUICK_RANDOM:
        from quicksort import quicksort_random
        plot_algorithm(ctx, quicksort_random)
    elif ctx.algorithm is SortingAlgorithm.SELECTION:
        from selection_sort import selection_sort
        plot_algorithm(ctx, selection_sort)
    else:
        raise NotImplementedError(
            'invalid sorting algorithm \'{}\''.format(ctx.algorithm))

if __name__ == '__main__':
    ctx = _get_context()
    init_clock()
    plot(ctx)
