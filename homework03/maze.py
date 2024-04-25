from copy import deepcopy
from random import choice, randint
from typing import List, Optional, Tuple, Union

import pandas as pd


def create_grid(rows: int = 15, cols: int = 15) -> List[List[Union[str, int]]]:
    return [["■"] * cols for _ in range(rows)]


def remove_wall(
    grid: List[List[Union[str, int]]], coord: Tuple[int, int]
) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param coord:
    :return:
    """
    # 1. выбрать любую клетку
    # 2. выбрать направление: наверх или направо.
    # Если в выбранном направлении следующая клетка лежит за границами поля,
    # выбрать второе возможное направление
    # 3. перейти в следующую клетку, сносим между клетками стену
    # 4. повторять 2-3 до тех пор, пока не будут пройдены все клетки

    for y,x in coord:
        size = len(grid)
        if y==1 and x<(size-2):
            grid[y][x+1] = " "
        if y > 1 and x < (size - 3):
            rr = randint (0,1)
            #print (rr)
            if rr ==0:
                grid[y][x + 1] = " "
            else:
                grid[y-1][x] = " "
        if y > 1 and x == (size-2):
            grid[y-1][x] = " "

    return grid


def bin_tree_maze(
    rows: int = 15, cols: int = 15, random_exit: bool = True
) -> List[List[Union[str, int]]]:
    """

    :param rows:
    :param cols:
    :param random_exit:
    :return:
    """

    grid = create_grid(rows, cols)
    empty_cells = []
    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            if x % 2 == 1 and y % 2 == 1:
                grid[x][y] = " "
                empty_cells.append((x, y))

#вызов функции сноса стен
    grid = remove_wall(grid,empty_cells)


    # генерация входа и выхода
    if random_exit:
        x_in, x_out = randint(0, rows - 1), randint(0, rows - 1)
        y_in = randint(0, cols - 1) if x_in in (0, rows - 1) else choice((0, cols - 1))
        y_out = randint(0, cols - 1) if x_out in (0, rows - 1) else choice((0, cols - 1))
    else:
        x_in, y_in = 0, cols - 2
        x_out, y_out = rows - 1, 1

    grid[x_in][y_in], grid[x_out][y_out] = "X", "X"

    return grid


def get_exits(grid: List[List[Union[str, int]]]) -> List[Tuple[int, int]]:
    """

    :param grid:
    :return:
    """

    exit_coords = [] #координаты входа/выхода
    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            if grid[x][y] == "X" or grid[x][y] == "1":
                exit_coords.append((x, y))
                #print (exit_coords)


    return exit_coords


def make_step(grid: List[List[Union[str, int]]], k: int) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param k:
    :return:
    """


    row = len(grid)

    exit_coords = get_exits(grid)
    print (exit_coords)
    print(row)
    x,y = exit_coords[0]
    if x == 0 and y >= 1:
        print('left',x,y)
    if y == 0 and x >= 1:
        print(x,y)
    if y == (row-1):
        print(x, y)
    if x == (row-1):
        print(x, y)

    return grid

#TTTttt
def shortest_path(
    grid: List[List[Union[str, int]]], exit_coord: Tuple[int, int]
) -> Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]:
    """

    :param grid:
    :param exit_coord:
    :return:
    """
    pass


def encircled_exit(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> bool:
    """

    :param grid:
    :param coord:
    :return:
    """

    pass


def solve_maze(
    grid: List[List[Union[str, int]]],
) -> Tuple[List[List[Union[str, int]]], Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]]:
    """

    :param grid:
    :return:
    """
# проверка если вход совпадает с выходом
    exit_coords = get_exits(grid)
    #print (len(exit_coords))
    if len(exit_coords) == 1: # если вход совпадает с выходом
        return grid, exit_coords

    y,x = exit_coords[0] # для первой координаты ставим 1
    grid[y][x] = "1"

# Заполняем нулями
    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            if grid[x][y] == " " or grid[x][y] == "X":
                grid[x][y] = 0

    k = 2
    grid = make_step(grid,k)

    return grid


def add_path_to_grid(
    grid: List[List[Union[str, int]]], path: Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]
) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param path:
    :return:
    """

    if path:
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                if (i, j) in path:
                    grid[i][j] = "X"
    return grid


if __name__ == "__main__":
    #print(pd.DataFrame(bin_tree_maze(15, 15)))
    GRID = bin_tree_maze(15, 15)
    #print(pd.DataFrame(GRID))
    FF = get_exits(GRID)
    print (FF)
    GREED2 = solve_maze(GRID)

    print(pd.DataFrame(GREED2))


    #_, PATH = solve_maze(GRID)
   # MAZE = add_path_to_grid(GRID, PATH)
   # print(pd.DataFrame(MAZE))
