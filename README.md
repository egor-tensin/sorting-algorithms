Sorting algorithms
==================

[![CI](https://github.com/egor-tensin/sorting-algorithms/actions/workflows/ci.yml/badge.svg)](https://github.com/egor-tensin/sorting-algorithms/actions/workflows/ci.yml)

Getting the hang out of (sorting) algorithms.
See also https://tensin.name/sorting-algorithms/.

Prerequisites
-------------

* Python 3.4 or higher
* [matplotlib]
* [numpy] (required by [matplotlib])

[matplotlib]: http://matplotlib.org/
[numpy]: http://www.numpy.org/

Algorithms
----------

Each of the implemented sorting algorithms resides in a separate Python module
(in the `algorithms.impl` package).
The implemented algorithms are listed below.

| Module name      | Description
| ---------------- | --------------
| `bubble_sort`    | Bubble sort
| `heapsort`       | Heapsort
| `insertion_sort` | Insertion sort
| `median`         | Median value
| `merge_sort`     | Merge sort
| `quicksort`      | Quicksort
| `selection_sort` | Selection sort

Some algorithms actually come in different variants.
For example, the implementation of quicksort includes a number of versions
depending on how the pivot element is chosen, be it the first, the second, the
middle, the last or a random element of the sequence.

Testing
-------

You can test each of the algorithms above by passing a sequence of integer
numbers to the corresponding script.

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

You can use the `algorithms.scripts.test` module to quickly generate an input
list of some kind and display the result of executing one of the implemented
algorithms.
Consult the output of `python -m algorithms.scripts.test --help` to learn how
to use the script.

```
> python -m algorithms.scripts.test --input best --length 1000 median_heaps
499.5
```

```
> python -m algorithms.scripts.test --input worst --length 10 quicksort_random
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Plotting
--------

You can generate similar plots you might've seen at
https://tensin.name/sorting-algorithms/ using the `algorithms.scripts.plot`
module.
Consult the output of `python -m algorithms.scripts.plot --help` to learn how
to use the script.

```
> python -m algorithms.scripts.plot merge_sort --min 0 --max 200 --input best --iterations 1000
```

```
> python -m algorithms.scripts.plot median_sorting --min 0 --max 200 --input average --iterations 100 --output median_sorting.png
```

If you're having problems using the script (like having excessive noise in the
measurement results), try minimizing background activity of your OS and
applications.

License
-------

Distributed under the MIT License.
See [LICENSE.txt] for details.

[LICENSE.txt]: LICENSE.txt
