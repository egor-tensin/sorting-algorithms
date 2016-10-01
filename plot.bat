@rem Copyright (c) 2015 Egor Tensin <Egor.Tensin@gmail.com>
@rem This file is part of the "Sorting algorithms" project.
@rem For details, see https://github.com/egor-tensin/sorting-algorithms.
@rem Distributed under the MIT License.

@setlocal enabledelayedexpansion
@echo off

set DEFAULT_ITERATIONS=100
set DEFAULT_MIN=0
set DEFAULT_MAX=200

if E%1 == E goto :exit_with_usage
set algorithm=%1

if not E%2 == E (
    set iterations=%2
) else (
    set iterations=%DEFAULT_ITERATIONS%
)
if not E%3 == E (
    set min=%3
) else (
    set min=%DEFAULT_MIN%
)
if not E%4 == E (
    set max=%4
) else (
    set max=%DEFAULT_MAX%
)

for %%i in (best average worst) do (
    plot.py "%algorithm%" ^
        --input "%%i" ^
        --min "%min%" --max "%max%" ^
        --iterations "%iterations%" ^
        --output "%algorithm%_%iterations%_%%i_%min%_%max%.png" || exit /b !errorlevel!
)

exit /b

:exit_with_usage:
echo Usage: %0 ALGORITHM [ITERATIONS=%DEFAULT_ITERATIONS% [MIN=%DEFAULT_MIN% [MAX=%DEFAULT_MAX%]]]
exit /b 1
