# Copyright 2016 Egor Tensin <Egor.Tensin@gmail.com>
# This file is licensed under the terms of the MIT License.
# See LICENSE.txt for details.

class Algorithm:
    def __init__(self, codename, display_name, f):
        self._codename = codename
        self._display_name = display_name
        self._f = f

    def get_codename(self):
        return self._codename

    def get_display_name(self):
        return self._display_name

    def get_function(self):
        return self._f

    def __str__(self):
        return self.get_display_name()

class SortingAlgorithm(Algorithm):
    def __init__(self, codename, display_name, f):
        super().__init__(codename, display_name, f)
