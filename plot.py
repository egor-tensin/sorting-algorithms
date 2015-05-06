# Copyright 2015 Egor Tensin <Egor.Tensin@gmail.com>
# This file is licensed under the terms of the MIT License.
# See LICENSE.txt for details.

from time import clock
import gc

_ALGORITHMS = (
    'bubble',
    'bubble_optimized',
    'heap',
    'insertion',
    'merge',
    'quick_first',
    'quick_second',
    'quick_middle',
    'quick_last',
    'quick_random',
    'selection',
)

def _get_context():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--repetitions', '-r', type=int, default=1,
                        help='set number of sorting repetitions')
    parser.add_argument('--input', '-i',
                        default='randomized', metavar='INPUT',
                        choices=('sorted', 'randomized', 'reversed'),
                        help='choose initial input state')
    parser.add_argument('--algorithm', '-l', metavar='ALGORITHM',
                        choices=_ALGORITHMS, required=True,
                        help='select sorting algorithm to use')
    parser.add_argument('--min', '-a', type=int, required=True,
                        help='set min input length',
                        dest='min_input_length')
    parser.add_argument('--max', '-b', type=int, required=True,
                        help='set max input length',
                        dest='max_input_length')
    parser.add_argument('--output', '-o', dest='plot_path',
                        help='set plot output path')
    args = parser.parse_args()
    if args.repetitions < 1:
        parser.error('number of repetitions must be > 0')
    if args.min_input_length < 0:
        parser.error('min sequence length must be >= 0')
    if args.max_input_length < 0:
        parser.error('max sequence length must be >= 0')
    if args.max_input_length < args.min_input_length:
        parser.error('max sequence length cannot be less than min sequence length')
    return args

def get_timestamp():
    return clock()

def init_clock():
    get_timestamp()

def gen_input(args, n):
    if args.input == 'sorted':
        return list(range(n))
    elif args.input == 'reversed':
        return sorted(range(n), reverse=True)
    elif args.input == 'randomized':
        from random import sample
        return sample(range(n), n)
    else:
        raise NotImplementedError(
            'unimplemented initial input state \'{}\''.format(args.input))

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
    if ctx.algorithm == 'bubble':
        from bubble_sort import bubble_sort
        plot_algorithm(ctx, bubble_sort)
    elif ctx.algorithm == 'bubble_optimized':
        from bubble_sort import bubble_sort_optimized
        plot_algorithm(ctx, bubble_sort_optimized)
    elif ctx.algorithm == 'heap':
        from heapsort import heapsort
        plot_algorithm(ctx, heapsort)
    elif ctx.algorithm == 'insertion':
        from insertion_sort import insertion_sort
        plot_algorithm(ctx, insertion_sort)
    elif ctx.algorithm == 'merge':
        from merge_sort import merge_sort
        plot_algorithm(ctx, merge_sort)
    elif ctx.algorithm == 'quick_first':
        from quicksort import quicksort_first
        plot_algorithm(ctx, quicksort_first)
    elif ctx.algorithm == 'quick_second':
        from quicksort import quicksort_second
        plot_algorithm(ctx, quicksort_second)
    elif ctx.algorithm == 'quick_middle':
        from quicksort import quicksort_middle
        plot_algorithm(ctx, quicksort_middle)
    elif ctx.algorithm == 'quick_last':
        from quicksort import quicksort_last
        plot_algorithm(ctx, quicksort_last)
    elif ctx.algorithm == 'quick_random':
        from quicksort import quicksort_random
        plot_algorithm(ctx, quicksort_random)
    elif ctx.algorithm == 'selection':
        from selection_sort import selection_sort
        plot_algorithm(ctx, selection_sort)
    else:
        raise NotImplementedError(
            'unknown algorithm \'{}\''.format(ctx.algorithm))

if __name__ == '__main__':
    ctx = _get_context()
    init_clock()
    plot(ctx)
