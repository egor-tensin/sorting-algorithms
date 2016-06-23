# Copyright 2016 Egor Tensin <Egor.Tensin@gmail.com>
# This file is licensed under the terms of the MIT License.
# See LICENSE.txt for details.

from numbers import Integral

from .inputgen import InputKind
from .plotter import PlotBuilder
from . import registry
from .timer import Timer

class AlgorithmParameters:
    def __init__(self, algorithm, min_len, max_len,
                 input_kind=InputKind.AVERAGE, iterations=1):

        if isinstance(algorithm, str):
            algorithm = registry.get(algorithm)
        self.algorithm = algorithm

        self.input_kind = input_kind

        self._min_len = None
        self._max_len = None
        self.min_len = min_len
        self.max_len = max_len

        self._iterations = None
        self.iterations = iterations

    @property
    def min_len(self):
        return self._min_len

    @min_len.setter
    def min_len(self, val):
        if not isinstance(val, Integral):
            raise TypeError('must be an integral value')
        val = int(val)
        if val < 0:
            raise ValueError('must not be a negative number')
        if self.max_len is not None and self.max_len < val:
            raise ValueError('must not be greater than the maximum length')
        self._min_len = val

    @property
    def max_len(self):
        return self._max_len

    @max_len.setter
    def max_len(self, val):
        if not isinstance(val, Integral):
            raise TypeError('must be an integral value')
        val = int(val)
        if val < 0:
            raise ValueError('must not be a negative number')
        if self.min_len is not None and self.min_len > val:
            raise ValueError('must not be lesser than the minimum length')
        self._max_len = val

    @property
    def iterations(self):
        return self._iterations

    @iterations.setter
    def iterations(self, val):
        if not isinstance(val, Integral):
            raise TypeError('must be an integral value')
        val = int(val)
        if val < 1:
            raise ValueError('must be a positive number')
        self._iterations = val

    def measure_running_time(self):
        input_len_range = list(range(self.min_len, self.max_len + 1))
        running_time = []
        for input_len in input_len_range:
            input_sample = self.algorithm.gen_input(input_len, self.input_kind)
            input_copies = [list(input_sample) for _ in range(self.iterations)]
            with Timer(running_time, self.iterations):
                for i in range(self.iterations):
                    self.algorithm.function(input_copies[i])
        return input_len_range, running_time

    @staticmethod
    def _format_plot_xlabel():
        return 'Input length'

    @staticmethod
    def _format_plot_ylabel():
        return 'Running time (sec)'

    def _format_plot_title(self):
        return '{}, {} case'.format(
            self.algorithm.display_name, self.input_kind)

    def _format_plot_suptitle(self):
        return self.algorithm.display_name

    def plot_running_time(self, output_path=None):
        plot_builder = PlotBuilder()
        plot_builder.show_grid()
        plot_builder.set_xlabel(self._format_plot_xlabel())
        plot_builder.set_ylabel(self._format_plot_ylabel())
        plot_builder.set_title(self._format_plot_title())
        xs, ys = self.measure_running_time()
        plot_builder.plot(xs, ys)
        if output_path is None:
            plot_builder.show()
        else:
            plot_builder.save(output_path)
