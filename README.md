Sorting algorithms
==================

Gettting the hang out of (sorting) algorithms.
The corresponding blog is hosted on [GitHub Pages] at
https://egor-tensin.github.io/sorting-algorithms/.

[GitHub Pages]: https://pages.github.com/

Prerequisites
-------------

Python 3.4 or higher is required.
Additionally, the excellent [matplotlib] library is required for plotting.
The versions the author is using are listed below.

Software     | Version
------------ | -------
Python       | 3.5.1
[matplotlib] | 1.5.1

Algorithms
----------

Each of the implemented sorting algorithms resides in a separate Python module
(in the `algorithms.impl` package).
The implemented algorithms are listed below.

Module name      | Description
---------------- | --------------
`bubble_sort`    | Bubble sort
`heapsort`       | Heapsort
`insertion_sort` | Insertion sort
`median`         | Median value
`merge_sort`     | Merge sort
`quicksort`      | Quicksort
`selection_sort` | Selection sort

Some algorithms actually come in different variants.
For example, the implementation of quicksort includes a number of versions
depending on how the pivot element is chosen, be it the first, the second, the
middle, the last or a random element of the sequence.

Testing
-------

You can test each of the algorithms above by passing a sequence of integer
numbers to the corresponding script.
Notice that you must invoke the scripts from the top-level directory using
`python -m`.
For example:

```
> python -m algorithms.impl.heapsort 5 3 4 1 2
[1, 2, 3, 4, 5]
```

```
> python -m algorithms.impl.quicksort 5 3 4 1 2
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
```

You can use "test.py" to quickly generate an input list of some kind and
display the result of executing one of the implemented algorithms.
Consult the output of `test.py --help` to learn how to use the script.
A few usage examples are listed below.

```
> test.py --input best --length 1000 median_heaps
499.5
```

```
> test.py --input worst --length 10 quicksort_random
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Plotting
--------

The goals of this "project" include a) familiarizing myself with a few sorting
algorithms by examining their (possibly, simplified) implementations and b)
studying the way algorithm's running time changes in relation to the length of
its input (a.k.a. identifying its time complexity).

A simple way to visualize the way algorithm's running time changes is to make
appropriate measurements and plot them on a nice graph.
The results of course are highly dependent on the hardware used, while the
graph's look depends on the software used for rendering.

I've made the measurements for each of the implemented algorithms and put the
plots to the "plots/" directory.
Both the hardware & the software that were used to produce the plots are listed
below.

Component    | Version
------------ | ---------------------
CPU          | [Intel Core i3-5005U]
OS           | Windows 8.1
Python       | 3.5.1
[matplotlib] | 1.5.1

[Intel Core i3-5005U]: http://ark.intel.com/products/84695/Intel-Core-i3-5005U-Processor-3M-Cache-2_00-GHz
[matplotlib]: http://matplotlib.org/

Each of the implemented sorting algorithms was provided with three input
sequences:

* a list of *n* consecutive numbers sorted in ascending order,
* ... in descending order,
* ... in random order.

You can generate similar plots using "plot.py".
Consult the output of `plot.py --help` to learn how to use the script.
A few usage examples are listed below.

```
> plot.py merge_sort --min 0 --max 200 --input best --iterations 1000
```

```
> plot.py median_sorting --min 0 --max 200 --input average --iterations 100 --output median_sorting.png
```

If you're having problems using the script (like having excessive noise in the
measurement results), try minimizing background activity of your OS and
applications.
For example, on Windows 8.1 I got very reasonable plots after booting into Safe
Mode and running the script with a higher priority while also setting its CPU
affinity:

```
> start /affinity 1 /realtime plot.py ...
```

License
-------

Distributed under the MIT License.
See [LICENSE.txt] for details.

[LICENSE.txt]: LICENSE.txt
