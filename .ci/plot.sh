#!/usr/bin/env bash

# Copyright (c) 2019 Egor Tensin <Egor.Tensin@gmail.com>                        
# This file is part of the "Sorting algorithms" project.                                
# For details, see https://github.com/egor-tensin/sorting-algorithms.                   
# Distributed under the MIT License.

set -o errexit -o nounset -o pipefail
shopt -s inherit_errexit lastpipe

script_dir="$( dirname -- "${BASH_SOURCE[0]}" )"
script_dir="$( cd -- "$script_dir" && pwd )"
readonly script_dir

declare -a algorithm_list=(
    bubble_sort
    bubble_sort_optimized
    heapsort
    insertion_sort
    merge_sort
    quicksort_first
    quicksort_last
    quicksort_middle
    quicksort_random
    quicksort_second
    selection_sort
)

fix_matplotlib() {
    # Get rid of:
    # tkinter.TclError: no display name and no $DISPLAY environment variable
    mkdir -p -- ~/.config/matplotlib
    echo 'backend: Agg' > ~/.config/matplotlib/matplotlibrc
}

main() {
    fix_matplotlib

    local algorithm
    for algorithm in ${algorithm_list[@]+"${algorithm_list[@]}"}; do
        echo "Plotting algorithm $algorithm..."
        "$script_dir/../plot.sh" "$algorithm"
    done
}

main "$@"
