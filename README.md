# Sorting algorithms

Gettting the hang out of sorting algorithms.
Hosted on [GitHub Pages](https://pages.github.com) at
https://egor-tensin.github.io/sorting_algorithms/.

## Algorithms

Each of the implemented sorting algorithms resides in a separate Python module.
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

               |                                                         |
-------------- | ------------------------------------------------------- |
**CPU**        | [Intel Atom N2800](http://ark.intel.com/products/58917) |
**OS**         | Windows 7 Professional Service Pack 1                   |
**Python**     | 3.4.1                                                   |
**matplotlib** | 1.4.0                                                   |

Each of the implemented algorithms was provided with three input sequences:
* a list of *n* consecutive numbers sorted in ascending order ("sorted" input),
* ... in descending order ("reversed" input),
* ... in random order ("randomized" input).

You can generate the plots using `plot.py`.
Consult the output of `plot.py -h` to learn how to use the script.

## Licensing

This project, including all of the files and their contents, is licensed under
the terms of the MIT License.
See [LICENSE.txt](LICENSE.txt) for details.
