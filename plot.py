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

def get_timestamp():
    return clock()

def init_clock():
    get_timestamp()

def gen_input(kind, n):
    if kind is InputKind.SORTED:
        return list(range(n))
    elif kind is InputKind.REVERSED:
        return sorted(range(n), reverse=True)
    elif kind is InputKind.RANDOMIZED:
        from random import sample
        return sample(range(n), n)
    else:
        raise NotImplementedError(
            'invalid initial input state \'{}\''.format(kind))

def measure_running_time(algorithm, kind, xs_len, repetitions):
    xs = gen_input(kind, xs_len)
    xss = [list(xs) for _ in range(repetitions)]
    algorithm = algorithm.get_function()
    gc.disable()
    started_at = get_timestamp()
    for i in range(repetitions):
        algorithm(xss[i])
    finished_at = get_timestamp()
    gc.enable()
    return finished_at - started_at

def _decorate_plot(algorithm, repetitions, kind, plt):
    plt.grid()
    plt.xlabel('Input length')
    plt.ylabel('Running time (sec)')
    plt.title('{}, {} repetition(s), {} input'.format(
        algorithm.get_display_name(), repetitions, kind))

def plot_algorithm(algorithm, repetitions, kind, min_len, max_len, output_path=None):
    import matplotlib.pyplot as plt
    _decorate_plot(algorithm, repetitions, kind, plt)
    xs_lengths = range(min_len, max_len + 1)
    running_time = []
    for xs_len in xs_lengths:
        running_time.append(measure_running_time(algorithm, kind, xs_len, repetitions))
    plt.plot(xs_lengths, running_time)
    if output_path is None:
        plt.show()
    else:
        plt.savefig(output_path)

if __name__ == '__main__':
    import algorithms.registry

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

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--algorithm', '-l', required=True,
                        choices=algorithms.registry.get_codenames(),
                        help='specify sorting algorithm to use')
    parser.add_argument('--repetitions', '-r',
                        type=positive_number, default=1,
                        help='set number of sorting repetitions')
    parser.add_argument('--input', '-i',
                        choices=tuple(x for x in InputKind),
                        type=input_kind, default=InputKind.RANDOMIZED,
                        help='choose initial input state')
    parser.add_argument('--min', '-a', type=natural_number,
                        required=True, dest='min_len',
                        help='set min input length')
    parser.add_argument('--max', '-b', type=natural_number,
                        required=True, dest='max_len',
                        help='set max input length')
    parser.add_argument('--output', '-o', dest='output_path',
                        help='set plot output path')
    args = parser.parse_args()
    if args.max_len < args.min_len:
        parser.error('max input length cannot be less than min input length')

    init_clock()
    plot_algorithm(algorithms.registry.get(args.algorithm),
                   args.repetitions, args.input,
                   args.min_len, args.max_len,
                   args.output_path)
