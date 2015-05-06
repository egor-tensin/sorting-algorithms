@rem Copyright 2015 Egor Tensin <Egor.Tensin@gmail.com>
@rem This file is licensed under the terms of the MIT License.
@rem See LICENSE.txt for details.

@setlocal enabledelayedexpansion

@if E%1 == E goto :print_usage
@set algorithm=%1

@if not E%2 == E (
  set repetitions=%2
) else (
  set repetitions=100
)
@if not E%3 == E (
  set min=%3
) else (
  set min=0
)
@if not E%4 == E (
  set max=%4
) else (
  set max=200
)

plot.py -l "%algorithm%" -a "%min%" -b "%max%" -r "%repetitions%" ^
    -i sorted     -o "%algorithm%_%repetitions%_sorted_%min%_%max%.png" ^
    || exit /b !errorlevel!
plot.py -l "%algorithm%" -a "%min%" -b "%max%" -r "%repetitions%" ^
    -i randomized -o "%algorithm%_%repetitions%_randomized_%min%_%max%.png" ^
    || exit /b !errorlevel!
plot.py -l "%algorithm%" -a "%min%" -b "%max%" -r "%repetitions%" ^
    -i reversed   -o "%algorithm%_%repetitions%_reversed_%min%_%max%.png" ^
    || exit /b !errorlevel!

@exit /b

:print_usage:
@echo Usage: %0 ALGORITHM [REPETITIONS [MIN [MAX]]]
@exit /b 1
