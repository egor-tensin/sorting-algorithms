# Copyright 2015 Egor Tensin <Egor.Tensin@gmail.com>
# This file is licensed under the terms of the MIT License.
# See LICENSE.txt for details.

from enum import Enum
import gc
import pylab
from time import clock

class OrderType(Enum):
    ASCENDING, RANDOM, DESCENDING = 'ascending', 'random', 'descending'

    def __str__(self):
        return self.value

    def get_case(self):
        if self is OrderType.ASCENDING:
            return 'best'
        elif self is OrderType.DESCENDING:
            return 'worst'
        elif self is OrderType.RANDOM:
            return 'average'
        else:
            raise NotImplementedError(
                'unknown "case" for input ordering: \'{}\''.format(self))

def get_timestamp():
    return clock()

def init_clock():
    get_timestamp()

def gen_input(order, n):
    if order is OrderType.ASCENDING:
        return list(range(n))
    elif order is OrderType.DESCENDING:
        return sorted(range(n), reverse=True)
    elif order is OrderType.RANDOM:
        from random import sample
        return sample(range(n), n)
    else:
        raise NotImplementedError(
            'invalid input ordering: \'{}\''.format(order))

def measure_running_time(algorithm, order, xs_len, iterations):
    xs = gen_input(order, xs_len)
    xss = [list(xs) for _ in range(iterations)]
    algorithm = algorithm.get_function()
    gc.disable()
    started_at = get_timestamp()
    for i in range(iterations):
        algorithm(xss[i])
    finished_at = get_timestamp()
    gc.enable()
    return finished_at - started_at

def _decorate_plot(algorithm, iterations, order):
    pylab.grid()
    pylab.xlabel("Input length")
    pylab.ylabel('Running time (sec), {} iteration(s)'.format(iterations))
    pylab.title("{}, {} case".format(
        algorithm.get_display_name(), order.get_case()))

def plot_algorithm(algorithm, iterations, order, min_len, max_len, output_path=None):
    _decorate_plot(algorithm, iterations, order)
    xs_lengths = range(min_len, max_len + 1)
    running_time = []
    for xs_len in xs_lengths:
        running_time.append(measure_running_time(algorithm, order, xs_len, iterations))
    pylab.plot(xs_lengths, running_time)
    if output_path is None:
        pylab.show()
    else:
        pylab.savefig(output_path)

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
            return OrderType(s)
        except ValueError:
            raise argparse.ArgumentError()

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--algorithm', '-l', required=True,
                        choices=algorithms.registry.get_codenames(),
                        help='specify sorting algorithm to use')
    parser.add_argument('--iterations', '-r',
                        type=positive_number, default=1,
                        help='set number of algorithm iterations')
    parser.add_argument('--order', '-i',
                        choices=tuple(x for x in OrderType),
                        type=input_kind, default=OrderType.RANDOM,
                        help='specify input order')
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
                   args.iterations, args.order,
                   args.min_len, args.max_len,
                   args.output_path)
