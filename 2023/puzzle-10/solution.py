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

        if pipe_str == 'S':
            self.start = True
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
        else:
            self.direction = None

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def get_next_direction(self, input_dir):
        try:
            return self.direction[input_dir]
        except KeyError:
            print(f'Direction Error: ')


class Grid:

    def __init__(self, input_matrix: List[List[str]]) -> None:
        self.container = []
        for y in range(len(input_matrix)):
            for x in range(len(input_matrix(y))):
                tile = Tile(input_matrix[y][x], x, y)
                self.container.append(tile)
                if input_matrix[y][x] == 'S':
                    self.start = tile

    def step(self, )
        


def part_1():
    with open('input.txt', 'r') as f:
        input_lines = f.readlines()  

    return None

def part_2():
    with open('input.txt', 'r') as f:
        input_lines = f.readlines()  

    return None

if __name__ == '__main__':
    print(part_1())
    # print(part_2())
