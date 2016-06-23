# Copyright 2016 Egor Tensin <Egor.Tensin@gmail.com>
# This file is licensed under the terms of the MIT License.
# See LICENSE.txt for details.

from . import impl

_ALL_ALGORITHMS = impl.refresh_algorithms()

def get_codenames():
    return _ALL_ALGORITHMS.keys()

def get(codename):
    return _ALL_ALGORITHMS[codename]
