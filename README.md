# Sorting algorithms

Gettting the hang out of sorting algorithms.
Hosted on [GitHub Pages](https://pages.github.com) at
https://egor-tensin.github.io/sorting_algorithms/.

## Algorithm implementations

Sorting algorithms are implemented in separate Python scripts.
You can test each of the implemented algorithms by passing a sequence of
integer numbers to the corresponding script.

Currently the following sorting algorithms are implemented:
* bubble sort (`bubble_sort.py`),
* heapsort (`heapsort.py`),
* insertion sort (`insertion_sort.py`),
* merge sort (`merge_sort.py`),
* selection sort (`selection_sort.py`),
* quicksort (`quicksort.py`).

Some scripts actually implement more than one version of a sorting algorithm.
For example, a quicksort is implemented in multiple versions depending on the
choice of the pivot element.

## Plots

Running time of the implemented sorting algorithms is measured and plotted.
The plots are stored in the `plots/` directory.

Each algorithm is provided with three lists:
* a list of sorted numbers,
* a reversed list of sorted numbers,
* and a list of numbers in random order.

## Usage

### Prerequisites

To use this software, you need to be able to run Python 3 scripts.

To plot a sorting algorithm, use `plot.py` (on Windows, you can also use
`plot.bat`, which simply calls `plot.py` three times, providing the sorting
algorithm with sorted, reversed, and randomized inputs).

## Licensing

This project, including all of the files and their contents, is licensed under
the terms of the MIT License.
See LICENSE.txt for details.
