# Copyright (c) 2016 Egor Tensin <Egor.Tensin@gmail.com>
# This file is part of the "Sorting algorithms" project.
# For details, see https://github.com/egor-tensin/sorting-algorithms.
# Distributed under the MIT License.

from . import impl


_ALL_ALGORITHMS = impl.refresh_algorithms()


def get_codenames():
    return _ALL_ALGORITHMS.keys()


def get(codename):
    return _ALL_ALGORITHMS[codename]
