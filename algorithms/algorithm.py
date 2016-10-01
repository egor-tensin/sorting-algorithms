# Copyright (c) 2016 Egor Tensin <Egor.Tensin@gmail.com>
# This file is part of the "Sorting algorithms" project.
# For details, see https://github.com/egor-tensin/sorting-algorithms.
# Distributed under the MIT License.

from . import inputgen

class Algorithm:
    def __init__(self, codename, display_name, f):
        self.codename = codename
        self.display_name = display_name
        self.function = f

    @staticmethod
    def gen_input(n, case=inputgen.InputKind.AVERAGE):
        #raise NotImplementedError('inputgen generation is not defined for generic algorithms')
        return inputgen.gen_input_for_sorting(n, case)

class SortingAlgorithm(Algorithm):
    def __init__(self, codename, display_name, f):
        super().__init__(codename, display_name, f)

    def gen_input(self, n, case=inputgen.InputKind.AVERAGE):
        return inputgen.gen_input_for_sorting(n, case)
