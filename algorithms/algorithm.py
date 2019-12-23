# Copyright (c) 2016 Egor Tensin <Egor.Tensin@gmail.com>
# This file is part of the "Sorting algorithms" project.
# For details, see https://github.com/egor-tensin/sorting-algorithms.
# Distributed under the MIT License.

from . import input_kind


class Algorithm:
    def __init__(self, codename, display_name, f):
        self.codename = codename
        self.display_name = display_name
        self.function = f

    @staticmethod
    def gen_input(n, case=input_kind.InputKind.AVERAGE):
        #raise NotImplementedError('input generation is not defined for a generic algorithm')
        return input_kind.gen_input_for_sorting(n, case)


class SortingAlgorithm(Algorithm):
    def gen_input(self, n, case=input_kind.InputKind.AVERAGE):
        return input_kind.gen_input_for_sorting(n, case)
