# Copyright 2016 Egor Tensin <Egor.Tensin@gmail.com>
# This file is licensed under the terms of the MIT License.
# See LICENSE.txt for details.

from enum import Enum

class OrderType(Enum):
    ASCENDING, RANDOM, DESCENDING = 'ascending', 'random', 'descending'

    def __str__(self):
        return self.value

def gen_input(kind, n):
    if kind is OrderType.ASCENDING:
        return list(range(n))
    elif kind is OrderType.DESCENDING:
        return sorted(range(n), reverse=True)
    elif kind is OrderType.RANDOM:
        from random import sample
        return sample(range(n), n)
    else:
        raise NotImplementedError(
            'invalid input ordering: \'{}\''.format(kind))

if __name__ == '__main__':
    import algorithms.registry

    def natural_number(s):
        n = int(s)
        if n < 0:
            raise argparse.ArgumentTypeError('cannot be negative')
        return n
    def order(s):
        try:
            return OrderType(s)
        except ValueError:
            raise argparse.ArgumentError()

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--algorithm', '-l', required=True,
                        choices=algorithms.registry.get_codenames(),
                        help='specify algorithm codename')
    parser.add_argument('--order', '-i',
                        choices=tuple(x for x in OrderType),
                        type=order, default=OrderType.RANDOM,
                        help='specify input order')
    parser.add_argument('--length', '-n',
                        type=natural_number, default=100,
                        help='set input length')
    args = parser.parse_args()
    xs = gen_input(args.order, args.length)
    print(algorithms.registry.get(args.algorithm).get_function()(xs))
