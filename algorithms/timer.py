# Copyright 2016 Egor Tensin <Egor.Tensin@gmail.com>
# This file is licensed under the terms of the MIT License.
# See LICENSE.txt for details.

import gc, time

def get_timestamp():
    return time.perf_counter()

class Timer:
    def __init__(self, dest, iterations=1):
        self._dest = dest
        self._iterations = iterations

    def __enter__(self):
        gc.disable()
        self._start = get_timestamp()
        return self

    def __exit__(self, *args):
        end = get_timestamp()
        gc.enable()
        self._dest.append((end - self._start) / self._iterations)
