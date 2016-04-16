# Copyright 2016 Egor Tensin <Egor.Tensin@gmail.com>
# This file is licensed under the terms of the MIT License.
# See LICENSE.txt for details.

from enum import Enum

class InputKind(Enum):
    SORTED, RANDOMIZED, REVERSED = 'sorted', 'randomized', 'reversed'

    def __str__(self):
        return self.value

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

if __name__ == '__main__':
    import algorithms.registry

    def natural_number(s):
        n = int(s)
        if n < 0:
            raise argparse.ArgumentTypeError('cannot be negative')
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
                        help='specify algorithm codename')
    parser.add_argument('--input', '-i',
                        choices=tuple(x for x in InputKind),
                        type=input_kind, default=InputKind.RANDOMIZED,
                        help='set initial input state')
    parser.add_argument('--length', '-n',
                        type=natural_number, default=100,
                        help='set input length')
    args = parser.parse_args()
    xs = gen_input(args.input, args.length)
    print(algorithms.registry.get(args.algorithm).get_function()(xs))
