# Copyright 2016 Egor Tensin <Egor.Tensin@gmail.com>
# This file is licensed under the terms of the MIT License.
# See LICENSE.txt for details.

from importlib import import_module
import os.path
from pkgutil import iter_modules

from .. import algorithm

_ALGORITHMS_NAME = '_ALGORITHMS'

def refresh_algorithms():
    all_algorithms = {}

    for _, module_name, is_pkg in iter_modules([os.path.dirname(__file__)]):
        if is_pkg:
            continue
        module = import_module('.' + module_name, __package__)
        if hasattr(module, _ALGORITHMS_NAME):
            module_algorithms = getattr(module, _ALGORITHMS_NAME)
            for descr in module_algorithms:
                assert isinstance(descr, algorithm.Algorithm)
                assert descr.codename not in all_algorithms
                all_algorithms[descr.codename] = descr

    return all_algorithms
