# Copyright 2016 Egor Tensin <Egor.Tensin@gmail.com>
# This file is licensed under the terms of the MIT License.
# See LICENSE.txt for details.

import algorithms.impl

def refresh_algorithms():
    algorithms.impl._refresh_algorithms()

def get_codenames():
    return algorithms.impl._ALL_ALGORITHMS.keys()

def iter_algorithms():
    return iter(algorithms.impl._ALL_ALGORITHMS.values())

def get(codename):
    return algorithms.impl._ALL_ALGORITHMS[codename]
