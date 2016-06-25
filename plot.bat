@rem Copyright 2015 Egor Tensin <Egor.Tensin@gmail.com>
@rem This file is licensed under the terms of the MIT License.
@rem See LICENSE.txt for details.

@setlocal enabledelayedexpansion

@set DEFAULT_ITERATIONS=100
@set DEFAULT_MIN=0
@set DEFAULT_MAX=200

@if E%1 == E goto :print_usage
@set algorithm=%1

@if not E%2 == E (
    set iterations=%2
) else (
    set iterations=%DEFAULT_ITERATIONS%
)
@if not E%3 == E (
    set min=%3
) else (
    set min=%DEFAULT_MIN%
)
@if not E%4 == E (
    set max=%4
) else (
    set max=%DEFAULT_MAX%
)

plot.py "%algorithm%" --min "%min%" --max "%max%" ^
    --iterations "%iterations%" --input best ^
    --output "%algorithm%_%iterations%_best_%min%_%max%.png" ^
    || exit /b !errorlevel!
plot.py "%algorithm%" --min "%min%" --max "%max%" ^
    --iterations "%iterations%" --input average ^
    --output "%algorithm%_%iterations%_average_%min%_%max%.png" ^
    || exit /b !errorlevel!
plot.py "%algorithm%" --min "%min%" --max "%max%" ^
    --iterations "%iterations%" --input worst ^
    --output "%algorithm%_%iterations%_worst_%min%_%max%.png" ^
    || exit /b !errorlevel!

@exit /b

:print_usage:
@echo Usage: %0 ALGORITHM [ITERATIONS=%DEFAULT_ITERATIONS% [MIN=%DEFAULT_MIN% [MAX=%DEFAULT_MAX%]]]
@exit /b 1
