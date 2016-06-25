# Copyright 2015 Egor Tensin <Egor.Tensin@gmail.com>
# This file is licensed under the terms of the MIT License.
# See LICENSE.txt for details.

import argparse
import sys

from algorithms.inputgen import InputKind
from algorithms.params import AlgorithmParameters
import algorithms.registry as registry

_DEFAULT_ITERATIONS = 100
_DEFAULT_INPUT_KIND = InputKind.AVERAGE
_DEFAULT_MIN_LENGTH = 0
_DEFAULT_MAX_LENGTH = 200

def plot_algorithm(algorithm, input_kind=_DEFAULT_INPUT_KIND,
                   min_len=_DEFAULT_MIN_LENGTH,
                   max_len=_DEFAULT_MAX_LENGTH,
                   iterations=_DEFAULT_ITERATIONS,
                   output_path=None):

    if isinstance(algorithm, str):
        algorithm = registry.get(algorithm)

    params = AlgorithmParameters(algorithm, min_len, max_len,
                                 input_kind=input_kind,
                                 iterations=iterations)
    params.plot_running_time(output_path)

def _parse_natural_number(s):
    try:
        n = int(s)
    except ValueError:
        raise argparse.ArgumentTypeError('must be a non-negative integer: ' + str(s))
    if n < 0:
        raise argparse.ArgumentTypeError('must be a non-negative integer')
    return n

def _parse_positive_number(s):
    try:
        n = int(s)
    except ValueError:
        raise argparse.ArgumentTypeError('must be a positive integer: ' + str(s))
    if n < 1:
        raise argparse.ArgumentTypeError('must be a positive integer')
    return n

def _parse_input_kind(s):
    try:
        return InputKind(s)
    except ValueError:
        raise argparse.ArgumentTypeError('invalid input kind: ' + str(s))

def _format_algorithm(codename):
    return '* {}: {}'.format(codename, registry.get(codename).display_name)

def _format_available_algorithms():
    descr = 'available algorithms (in the CODENAME: DISPLAY_NAME format):\n'
    return descr + '\n'.join(map(
        _format_algorithm, sorted(registry.get_codenames())))

def _format_description():
    return _format_available_algorithms()

def _create_argument_parser():
    return argparse.ArgumentParser(
        description=_format_description(),
        formatter_class=argparse.RawDescriptionHelpFormatter)

def _parse_args(args=sys.argv):
    parser = _create_argument_parser()

    parser.add_argument('algorithm', metavar='CODENAME',
                        choices=registry.get_codenames(),
                        help='algorithm codename')
    parser.add_argument('--iterations', '-r', metavar='N',
                        type=_parse_positive_number,
                        default=_DEFAULT_ITERATIONS,
                        help='set number of algorithm iterations')
    parser.add_argument('--input', '-i', dest='input_kind',
                        choices=InputKind,
                        type=_parse_input_kind, default=_DEFAULT_INPUT_KIND,
                        help='specify input kind')
    parser.add_argument('--min', '-a', metavar='N', dest='min_len',
                        type=_parse_natural_number,
                        default=_DEFAULT_MIN_LENGTH,
                        help='set min input length')
    parser.add_argument('--max', '-b', metavar='N', dest='max_len',
                        type=_parse_natural_number,
                        default=_DEFAULT_MAX_LENGTH,
                        help='set max input length')
    parser.add_argument('--output', '-o', metavar='PATH', dest='output_path',
                        help='set plot file path')

    return parser.parse_args(args[1:])

def main(args=sys.argv):
    plot_algorithm(**vars(_parse_args(args)))

if __name__ == '__main__':
    main()
