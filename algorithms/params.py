# Copyright (c) 2016 Egor Tensin <Egor.Tensin@gmail.com>
# This file is part of the "Sorting algorithms" project.
# For details, see https://github.com/egor-tensin/sorting-algorithms.
# Distributed under the MIT License.

from enum import Enum
from numbers import Integral

from .input_kind import InputKind
from .plotter import PlotBuilder
from . import registry
from .timer import Timer


class TimeUnits(Enum):
    SECONDS = 'seconds'
    MILLISECONDS = 'milliseconds'
    MICROSECONDS = 'microseconds'

    def get_factor(self):
        if self is TimeUnits.SECONDS:
            return 1.
        if self is TimeUnits.MILLISECONDS:
            return 1000.
        if self is TimeUnits.MICROSECONDS:
            return 1000000.
        raise NotImplementedError('invalid time units: ' + str(self))

    def __str__(self):
        return self.value


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
            raise ValueError('must be non-negative')
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
            raise ValueError('must be non-negative')
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
            raise ValueError('must be positive')
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
    def _format_plot_ylabel(units):
        return 'Running time ({})'.format(units)

    def _format_plot_title(self):
        return '{}, {} case'.format(
            self.algorithm.display_name, self.input_kind)

    def _format_plot_suptitle(self):
        return self.algorithm.display_name

    @staticmethod
    def _derive_time_units(ys):
        max_y = max(ys)
        if max_y > 0.1:
            return TimeUnits.SECONDS
        if max_y > 0.0001:
            return TimeUnits.MILLISECONDS
        return TimeUnits.MICROSECONDS

    def plot_running_time(self, output_path=None):
        xs, ys = self.measure_running_time()
        units = self._derive_time_units(ys)
        ys = [y * units.get_factor() for y in ys]

        plot_builder = PlotBuilder()
        plot_builder.show_grid()
        plot_builder.set_xlabel(self._format_plot_xlabel())
        plot_builder.set_ylabel(self._format_plot_ylabel(units))
        #plot_builder.set_yticklabels_scientific()
        plot_builder.set_title(self._format_plot_title())
        plot_builder.plot(xs, ys)
        if output_path is None:
            plot_builder.show()
        else:
            plot_builder.save(output_path)
