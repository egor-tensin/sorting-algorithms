# Copyright 2016 Egor Tensin <Egor.Tensin@gmail.com>
# This file is licensed under the terms of the MIT License.
# See LICENSE.txt for details.

_ALL_ALGORITHMS = {}

def _refresh_algorithms():
    _ALGORITHMS_NAME = '_ALGORITHMS'
    global _ALL_ALGORITHMS
    _ALL_ALGORITHMS = {}

    from algorithms.algorithm import Algorithm

    from importlib import import_module
    import os.path
    from pkgutil import iter_modules

    for _, module_name, is_pkg in iter_modules([os.path.dirname(__file__)]):
        if is_pkg:
            continue
        module = import_module('.' + module_name, __package__)
        if hasattr(module, _ALGORITHMS_NAME):
            module_algorithms = getattr(module, _ALGORITHMS_NAME)
            for algorithm in module_algorithms:
                assert isinstance(algorithm, Algorithm)
                assert algorithm.get_codename() not in _ALL_ALGORITHMS
                _ALL_ALGORITHMS[algorithm.get_codename()] = algorithm

_refresh_algorithms()
