import os
import sys
import time
from datetime import datetime
from typing import List, Union
import math
import concurrent.futures

class Tile:

    def __init__(self, pipe_str: str, x_coord: int, y_coord: int) -> None:
        self.x = x_coord
        self.y = y_coord

        self.is_loop = False

        if pipe_str == 'S':
            self.start = True
            self.is_loop = True
        else:
            self.start = False

        if pipe_str == '|':
            self.direction_1 = 'n'
            self.direction_2 = 's'
        elif pipe_str == '-':
            self.direction_1 = 'e'
            self.direction_2 = 'w'
        elif pipe_str == 'L':
            self.direction_1 = 'n'
            self.direction_2 = 'e'
        elif pipe_str == 'J':
            self.direction_1 = 'n'
            self.direction_2 = 'w'
        elif pipe_str == '7':
            self.direction_1 = 's'
            self.direction_2 = 'w'
        elif pipe_str == 'F':
            self.direction_1 = 's'
            self.direction_2 = 'e'
        else:
            self.direction_1 = None
            self.direction_2 = None

        if self.direction_1:
            self.direction = {
                self.direction_1: self.direction_2,
                self.direction_2: self.direction_1
            }
        elif pipe_str == 'S':
            self.direction = {
                'n': 'n',
                's': 's',
                'e': 'e',
                'w': 'w'
            }
        else:
            self.direction = None

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self) -> str:
        return f'({self.x},{self.y}):\t{self.direction_1}, {self.direction_2}'
    
    def get_next_direction(self, input_dir: str) -> Union[str, None]:
        try:
            return self.direction[input_dir]
        except KeyError:
            print(f'Direction Error: {self} has no direction {input_dir}')
            return None

    def reset_start(self, direction_1: str, direction_2: str) -> None:
        if self.start:
            self.direction_1 = direction_1
            self.direction_2 = direction_2
            self.direction = {
                self.direction_1: self.direction_2,
                self.direction_2: self.direction_1
            }


class Grid:

    def __init__(self, input_matrix: List[str]) -> None:
        self.container = []
        for y in range(len(input_matrix)):
            self.container.append([])
            for x in range(len(input_matrix[y])):
                tile = Tile(input_matrix[y][x], x, y)
                self.container[y].append(tile)
                if input_matrix[y][x] == 'S':
                    self.start = tile

    def get_tile_by_coords(self, x: int, y: int) -> Union[Tile, None]:
        try:
            return self.container[y][x]
        except IndexError:
            print('Grid out of Bounds Error')
            return None
        
    def get_start_tile(self, start_dir: str) -> Tile:
        if start_dir == 'n':
            return self.get_tile_by_coords(self.start.x, self.start.y-1), 's'
        elif start_dir == 's':
            return self.get_tile_by_coords(self.start.x, self.start.y+1), 'n'
        elif start_dir == 'e':
            return self.get_tile_by_coords(self.start.x+1, self.start.y), 'e'
        elif start_dir == 'w':
            return self.get_tile_by_coords(self.start.x-1, self.start.y), 'w'
        else:
            print('Invalid Direction Error')
            return None

    def step(self, tile: Tile, prev_direction: str):
        direction = tile.get_next_direction(prev_direction)
        if not direction:
            return None
        
        if direction == 'n':
            return self.get_tile_by_coords(tile.x, tile.y-1), 's'
        elif direction == 's':
            return self.get_tile_by_coords(tile.x, tile.y+1), 'n'
        elif direction == 'e':
            return self.get_tile_by_coords(tile.x+1, tile.y), 'w'
        elif direction == 'w':
            return self.get_tile_by_coords(tile.x-1, tile.y), 'e'
        else:
            print('Invalid Direction Error')
            return None


def walk_grid(grid: Grid, start_direction: str) -> int:
    loop_count = 0
    tile, prev_direction = grid.get_start_tile(start_direction)
    
    while tile != grid.start:
        loop_count += 1
        tile, prev_direction = grid.step(tile, prev_direction)
        tile.is_loop = True
        if not tile:
            return 0

    return loop_count

def count_inner_cells(grid: Grid):
    loop_count = 0
    for y in range(len(grid.container)):
        in_loop = False
        for x in range(len(grid.container[y])):

            # Check if up-pointing member of loop - If so then flip the in loop flag
            tile = grid.container[y][x]
            if tile.is_loop and 'n' in tile.direction.keys():
                in_loop = not in_loop
            
            # Check if in loop and cell is not part of the loop
            if in_loop and not tile.is_loop:
                loop_count += 1

    return loop_count


def part_1():
    with open('input.txt', 'r') as f:
        input_lines = f.readlines()  

    grid = Grid(input_lines)

    start_directions = ['n','e','s','w']
    loop_counts = []

    for d in start_directions:
        try:
            loop_counts.append(walk_grid(grid, d))
        except Exception as e:
            print(f'{d}:\t{e}')

    print(loop_counts)

    return sum(loop_counts) // 4 + 1

def part_2():
    with open('input.txt', 'r') as f:
        input_lines = f.readlines()  

    grid = Grid(input_lines)

    start_directions = ['n','e','s','w']
    loop_dirs = []

    # Walk the Loop
    for d in start_directions:
        try:
            _ = walk_grid(grid, d)
            loop_dirs.append(d)
        except Exception as e:
            print(f'{d}:\t{e}')

    # Reset the start node to an actual pipe
    grid.start.reset_start(loop_dirs[0], loop_dirs[1])

    # Check each tile for if it is in loop
    return count_inner_cells(grid)

if __name__ == '__main__':
    # print(part_1())
    print(part_2())
