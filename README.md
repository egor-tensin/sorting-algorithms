# Sorting algorithms

Gettting the hang out of (sorting) algorithms.
Hosted on [GitHub Pages](https://pages.github.com) at
https://egor-tensin.github.io/sorting_algorithms/.

## Algorithms

Each of the implemented sorting algorithms resides in a separate Python module
(in the `algorithms.impl` package).
Currently the following algorithms are implemented:

* bubble sort (`bubble_sort.py`),
* heapsort (`heapsort.py`),
* insertion sort (`insertion_sort.py`),
* merge sort (`merge_sort.py`),
* quicksort (`quicksort.py`),
* selection sort (`selection_sort.py`).

You can test each of the algorithms above by passing a sequence of integer
numbers to the corresponding script:

    > heapsort.py 5 3 4 1 2
    [1, 2, 3, 4, 5]

Some algorithms actually come in different variants.
For example, the implementation of quicksort includes a number of versions
depending on how the pivot element is chosen, be it the first, the second, the
middle, the last or a random element of the sequence.

    > quicksort.py 5 3 4 1 2
    [1, 2, 3, 4, 5]
    [1, 2, 3, 4, 5]
    [1, 2, 3, 4, 5]
    [1, 2, 3, 4, 5]
    [1, 2, 3, 4, 5]

You can use the generic script `test.py` to quickly generate an input list of
some kind and display the result of executing an algorithm on this input.
Consult the output of `test.py -h` to learn how to use the script.

## Plots

The goals of this "project" include a) familiarizing myself with a few sorting
algorithms by examining their (possibly, simplified) implementations and b)
studying the way algorithm's running time changes in relation to the length of
its input (a.k.a. identifying its time complexity).

A simple way to visualize the way algorithm's running time changes would be to
make appropriate measurements and plot them on a nice graph.
The results of course are highly dependent on the hardware used, while the
graph's look depends on the software used for rendering.

I've made the measurements for each of the implemented algorithms and put the
plots to the `plots/` directory.
Both the hardware & the software that were used to produce the plots are listed
below.

               |                                                                                                            |
-------------- | ---------------------------------------------------------------------------------------------------------- |
**CPU**        | [Intel Core i3-5005U](http://ark.intel.com/products/84695/Intel-Core-i3-5005U-Processor-3M-Cache-2_00-GHz) |
**OS**         | Windows 8.1                                                                                                |
**Python**     | 3.5.1                                                                                                      |
**matplotlib** | 1.5.1                                                                                                      |

Each of the implemented algorithms was provided with three input sequences:
* a list of *n* consecutive numbers sorted in ascending order ("sorted" input),
* ... in descending order ("reversed" input),
* ... in random order ("randomized" input).

You can generate the plots using `plot.py`.
Consult the output of `plot.py -h` to learn how to use the script.

If you're having problems using the script (like having excessive noise in the
measurement results), try minimizing background activity of the OS and the
applications.
For example, on Windows 8.1 I managed to produce some very nice plots by
booting into Safe Mode and running the scripts with a higher priority while
also setting their CPU affinity:

    start /affinity 1 /realtime calc_mean.py

## Licensing

This project, including all of the files and their contents, is licensed under
the terms of the MIT License.
See [LICENSE.txt](LICENSE.txt) for details.
