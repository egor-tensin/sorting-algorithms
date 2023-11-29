# Copyright (c) 2016 Egor Tensin <Egor.Tensin@gmail.com>
# This file is part of the "Sorting algorithms" project.
# For details, see https://github.com/egor-tensin/sorting-algorithms.
# Distributed under the MIT License.

import matplotlib.pyplot as plt


class PlotBuilder:
    def __init__(self):
        self._fig, self._ax = plt.subplots(figsize=(8, 6), dpi=200)
        self._ax.grid(alpha=0.8, linestyle=':')

    def plot(self, title, xlabel, ylabel, xs, ys):
        self._ax.set_title(title)
        self._ax.set_xlabel(xlabel)
        self._ax.set_ylabel(ylabel)
        self._ax.plot(xs, ys)

    @staticmethod
    def show():
        plt.show()

    def save(self, output_path):
        self._fig.savefig(output_path)
