# Copyright (c) 2016 Egor Tensin <Egor.Tensin@gmail.com>
# This file is part of the "Sorting algorithms" project.
# For details, see https://github.com/egor-tensin/sorting-algorithms.
# Distributed under the MIT License.

import matplotlib.pyplot as plt


class PlotBuilder:
    @staticmethod
    def set_xlabel(s):
        plt.xlabel(s)

    @staticmethod
    def set_ylabel(s):
        plt.ylabel(s)

    @staticmethod
    def set_yticklabels_scientific():
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))

    @staticmethod
    def show_grid():
        plt.grid()

    @staticmethod
    def set_title(s):
        plt.title(s)

    @staticmethod
    def set_suptitle(s):
        plt.suptitle(s)

    @staticmethod
    def plot(xs, ys):
        plt.plot(xs, ys)

    @staticmethod
    def show():
        plt.show()

    @staticmethod
    def save(output_path, tight=False):
        if tight:
            plt.savefig(output_path, bbox_inches='tight')
        else:
            plt.savefig(output_path)
