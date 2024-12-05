@echo off
setlocal enabledelayedexpansion

:: Check if Python 3.11 is installed
py -3.11 --version >nul 2>&1
if errorlevel 1 (
    echo Python 3.11 is not installed on this system.
    echo Please install Python 3.11 to proceed.
    timeout /t 5
    exit
)

:: Define maze names
set mazes=bigCorners bigMaze bigSafeSearch bigSearch boxSearch capsuleClassic contestClassic contoursMaze greedySearch mediumClassic mediumCorners mediumDottedMaze mediumMaze mediumSafeSearch mediumScaryMaze mediumSearch minimaxClassic oddSearch openClassic openMaze openSearch originalClassic powerClassic smallClassic smallMaze smallSafeSearch smallSearch testClassic testMaze testSearch tinyCorners tinyMaze tinySafeSearch tinySearch trappedClassic trickyClassic trickySearch

:: Define algorithms
set algorithms=bfs dfs astar ucs

:menu
cls
echo ================================
echo      Pac-Man Maze Solver
echo ================================
echo Select an option:
echo 1. Run the game interactively (no parameters)
echo 2. Solve a maze with parameters
echo 3. Run autograder
echo 4. Exit
echo ================================
set /p main_choice="Enter your choice: "

if "%main_choice%"=="1" (
    call py -3.11 ./pacman.py
    pause
    goto menu
) else if "%main_choice%"=="2" (
    goto select_maze
) else if "%main_choice%"=="3" (
    call py -3.11 ./autograder.py
    pause
    goto menu
) else if "%main_choice%"=="4" (
    exit
) else (
    echo Invalid choice. Please try again.
    pause
    goto menu
)

:select_maze
cls
echo ================================
echo Select a maze:
set count=0
for %%m in (%mazes%) do (
    set /a count+=1
    echo !count!. %%m
)
set /a count+=1
echo !count!. Back to Main Menu
echo ================================
set /p maze_choice="Enter your choice: "

set count=0
for %%m in (%mazes%) do (
    set /a count+=1
    if "%maze_choice%"=="!count!" (
        set maze=%%m
        goto select_algorithm
    )
)

:: Back to menu
set /a count+=1
if "%maze_choice%"=="!count!" (
    goto menu
)

echo Invalid choice. Please try again.
pause
goto select_maze

:select_algorithm
cls
echo ================================
echo Select an algorithm:
set count=0
for %%a in (%algorithms%) do (
    set /a count+=1
    echo !count!. %%a
)
set /a count+=1
echo !count!. Back to Main Menu
echo ================================
set /p algo_choice="Enter your choice: "

set count=0
for %%a in (%algorithms%) do (
    set /a count+=1
    if "%algo_choice%"=="!count!" (
        set algorithm=%%a
        goto run_solver
    )
)

:: Back to menu
set /a count+=1
if "%algo_choice%"=="!count!" (
    goto menu
)

echo Invalid choice. Please try again.
pause
goto select_algorithm

:run_solver
cls
echo Running the Pac-Man solver with the following parameters:
echo Maze: %maze%
echo Agent: SearchAgent
echo Algorithm: %algorithm%
call py -3.11 ./pacman.py -l %maze% -p SearchAgent -a fn=%algorithm%
pause

:retry
cls
echo ================================
echo Do you want to:
echo 1. Try another maze
echo 2. Try another algorithm
echo 3. Exit
echo ================================
set /p retry="Enter your choice: "

if "%retry%"=="1" (
    goto select_maze
) else if "%retry%"=="2" (
    goto select_algorithm
) else if "%retry%"=="3" (
    exit
) else (
    echo Invalid choice. Please try again.
    pause
    goto retry
)
