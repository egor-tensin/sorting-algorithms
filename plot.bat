@rem Copyright (c) 2015 Egor Tensin <Egor.Tensin@gmail.com>
@rem This file is part of the "Sorting algorithms" project.
@rem For details, see https://github.com/egor-tensin/sorting-algorithms.
@rem Distributed under the MIT License.

@setlocal enabledelayedexpansion
@echo off

set default_iterations=100
set default_min=0
set default_max=200

if "%~1" == "" goto :exit_with_usage
set "algorithm=%~1"

if "%~2" == "" (
    set "iterations=%default_iterations%"
) else (
    set "iterations=%~2"
)
if "%~3" == "" (
    set "min=%default_min%"
) else (
    set "min=%~3"
)
if "%~4" == "" (
    set "max=%default_max%"
) else (
    set "max=%~4"
)

for %%i in (best average worst) do (
    plot.py "%algorithm%" ^
        --input "%%i" ^
        --min "%min%" --max "%max%" ^
        --iterations "%iterations%" ^
        --output "%algorithm%_%iterations%_%%i_%min%_%max%.png" || exit /b !errorlevel!
)

exit /b 0

:exit_with_usage:
echo Usage: %~nx0 ALGORITHM [ITERATIONS [MIN_VALUE [MAX_VALUE]]]
exit /b 1
