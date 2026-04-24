# X = Wall
# . = Point
# O = Power Point

from constants import (CELL_SIZE, MAZE_GRID_ROWS, MAZE_GRID_COLUMNS,
                        MAZE_LEVEL_START_X, MAZE_LEVEL_START_Y)

maze_level_1 = [
    "XXXXXXXXXXXXXXXX.XXXXXXXXXXXXXXXX",
    "X..............................OX",
    "X.XXX.XXX.XXXXXX.XXXXXX.XXX.XXX.X",
    "X.X X.X X.X    X.X    X.X X.X X.X",
    "X.XXX.X X.XXXXXX.XXXXXX.X X.XXX.X",
    "X.....XXX.X....X.X....X.XXX.....X",
    "XXXXX.......XX.X.X.XX.......XXXXX",
    "X.....XXXXX...........XXXXX.....X",
    "X.XXX.......XXXXXXXXX.......XXX.X",
    "X.....XXXXX...........XXXXX.....X",
    "X.XXX...O...XXXX.XXXX.......XXX.X",
    "X.X X.XXXXX.X  X.X  X.XXXXX.X X.X",
    "X.X X.X   X.X  X.X  X.X   X.X X.X",
    "X.X X.X   X.X  X.X  X.X   X.X X.X",
    "X.X X.XXXXX.X  X.X  X.XXXXX.X X.X",
    "X.XXX.......XXXX.XXXX...O...XXX.X",
    "X.....XXXXX...........XXXXX.....X",
    "X.XXX.......XXXXXXXXX.......XXX.X",
    "X.....XXXXX...........XXXXX.....X",
    "XXXXX.......XX.X.X.XX.......XXXXX",
    "X.....XXX.X....X.X....X.XXX.....X",
    "X.XXX.X X.XXXXXX.XXXXXX.X X.XXX.X",
    "X.X X.X X.X    X.X    X.X X.X X.X",
    "X.XXX.XXX.XXXXXX.XXXXXX.XXX.XXX.X",
    "XO..............................X",
    "XXXXXXXXXXXXXXXX.XXXXXXXXXXXXXXXX"
] 

def calculate_maze_data(maze_level):
    walls = []
    points = []
    power_points = []

    for row in range(MAZE_GRID_ROWS):

        for col in range(MAZE_GRID_COLUMNS):
            pixel = maze_level[row][col]
            pixel_cor_x = MAZE_LEVEL_START_X + CELL_SIZE * col
            pixel_cor_y = MAZE_LEVEL_START_Y - CELL_SIZE * row

            if pixel == 'X':
                walls.append((pixel_cor_x,pixel_cor_y))
            elif pixel == '.':
                points.append((pixel_cor_x,pixel_cor_y))
            elif pixel == 'O':
                power_points.append((pixel_cor_x,pixel_cor_y))

    return walls, points, power_points