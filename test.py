# Copyright 2016 Egor Tensin <Egor.Tensin@gmail.com>
# This file is licensed under the terms of the MIT License.
# See LICENSE.txt for details.

from array import array
import argparse
import sys

from algorithms.inputgen import InputKind
import algorithms.registry as registry

_DEFAULT_INPUT_KIND = InputKind.AVERAGE
_DEFAULT_LENGTH = 100

def test(algorithm, input_kind=_DEFAULT_INPUT_KIND, length=_DEFAULT_LENGTH):
    if isinstance(algorithm, str):
        algorithm = registry.get(algorithm)
    xs = algorithm.gen_input(length, input_kind)
    output = algorithm.function(xs)
    if isinstance(output, array):
        output = output.tolist()
    print(output)

def _parse_natural_number(s):
    try:
        n = int(s)
    except ValueError:
        raise argparse.ArgumentTypeError('must be a non-negative integer: ' + str(s))
    if n < 0:
        raise argparse.ArgumentTypeError('must be a non-negative integer')
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

def _parse_args(args=sys.argv):
    parser = argparse.ArgumentParser(
        description=_format_description(),
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('algorithm', metavar='CODENAME',
                        choices=registry.get_codenames(),
                        help='algorithm codename')
    parser.add_argument('--input', '-i', dest='input_kind',
                        choices=InputKind,
                        type=_parse_input_kind, default=_DEFAULT_INPUT_KIND,
                        help='specify input kind')
    parser.add_argument('--length', '-l', '-n', metavar='N',
                        type=_parse_natural_number, default=_DEFAULT_LENGTH,
                        help='set input length')

    return parser.parse_args(args[1:])

def main(args=sys.argv):
    test(**vars(_parse_args(args)))

if __name__ == '__main__':
    main()