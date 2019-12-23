# Copyright (c) 2016 Egor Tensin <Egor.Tensin@gmail.com>
# This file is part of the "Sorting algorithms" project.
# For details, see https://github.com/egor-tensin/sorting-algorithms.
# Distributed under the MIT License.

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
