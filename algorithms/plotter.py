# Copyright 2016 Egor Tensin <Egor.Tensin@gmail.com>
# This file is licensed under the terms of the MIT License.
# See LICENSE.txt for details.

import matplotlib.pyplot as plt

class PlotBuilder:
    @staticmethod
    def set_xlabel(s):
        plt.xlabel(s)

    @staticmethod
    def set_ylabel(s):
        plt.ylabel(s)

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
    def save(output_path):
        plt.savefig(output_path)#, bbox_inches='tight')
