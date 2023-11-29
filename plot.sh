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
script_name="$( basename -- "${BASH_SOURCE[0]}" )"
readonly script_name

readonly default_iterations=100
readonly default_min=0
readonly default_max=200

main() {
    if [ "$#" -lt 1 ] || [ "$#" -gt 4 ]; then
        echo "usage: $script_name ALGORITHM [ITERATIONS [MIN_VALUE [MAX_VALUE]]]" >&2
        exit 1
    fi

    local algorithm="$1"
    local iterations="$default_iterations"
    [ "$#" -ge 2 ] && iterations="$2"
    local min="$default_min"
    [ "$#" -ge 3 ] && min="$3"
    local max="$default_max"
    [ "$#" -ge 4 ] && max="$4"

    mkdir -p -- "$script_dir/img"

    local input_kind
    for input_kind in best average worst; do
        local output_name="${algorithm}_${iterations}_${input_kind}_${min}_${max}.png"
        python "$script_dir/plot.py"   \
            "$algorithm"               \
            --input "$input_kind"      \
            --min "$min" --max "$max"  \
            --iterations "$iterations" \
            --output "$script_dir/img/$output_name"
    done
}

main "$@"
