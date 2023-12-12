import os
import sys
import time
from datetime import datetime
from typing import List, Union
import math
import concurrent.futures

def max_and_min(num1: int, num2: int) -> int:
    if num1 >= num2:
        return num1, num2
    else:
        return num2, num1

class Universe:

    def __init__(self, universe_rows: List[str]) -> None:

        # Expand Universe at init time
        # new_universe = []
        # column_planet_counts = [0] * (len(universe_rows[0])-1)
        # for r in range(len(universe_rows)):
        #     row_planet_count = 0
        #     row = universe_rows[r]
        #     for i in range(len(row)):
        #         if row[i] == '#':
        #             column_planet_counts[i] += 1
        #             row_planet_count += 1
            
        #     # If the row had no planets, add it to the new universe twice to expand
        #     if row_planet_count == 0:
        #         new_universe.append(row)
        #     new_universe.append(row)
        
        # # If the column had no plants , expand every row at that point with a period
        # col_expansion_index = [c for c in range(len(column_planet_counts)) if column_planet_counts[c] == 0]
        # for r in range(len(new_universe)):
        #     for c in range(len(col_expansion_index)):
        #         expansion_col = col_expansion_index[c] + c
        #         new_universe[r] = new_universe[r][:expansion_col] + '.' + new_universe[r][expansion_col:]

        self.universe = universe_rows
        self.planets = []
        self.empty_rows = []
        column_planet_counts = [0] * (len(universe_rows[0])-1)

        # Add array of planet coordinates
        for y in range(len(self.universe)):
            empty_row = True
            for x in range(len(self.universe[y])):
                if self.universe[y][x] == '#':
                    self.planets.append((x, y))
                    empty_row = False
                    column_planet_counts[x] += 1
            if empty_row:
                self.empty_rows.append(y)
        self.empty_cols = [c for c in range(len(column_planet_counts)) if column_planet_counts[c] == 0]

    def __str__(self) -> str:
        return_str = ''
        for r in self.universe:
            return_str = return_str + f'{r}\n'
        return return_str

    def calculate_paths(self, expansion_factor: int = 1) -> List[int]:
        expansion_factor -= 1
        lengths_array = []
        for p in range(len(self.planets)-1):
            planet_p = self.planets[p]
            for o in range(p+1, len(self.planets), 1):
                planet_o = self.planets[o]

                x_max, x_min = max_and_min(planet_p[0], planet_o[0])
                x_add_factor = 0
                for e in self.empty_cols:
                    if e >= x_min and e <= x_max:
                        x_add_factor += expansion_factor

                y_max, y_min = max_and_min(planet_p[1], planet_o[1])
                y_add_factor = 0
                for e in self.empty_rows:
                    if e >= y_min and e <= y_max:
                        y_add_factor += expansion_factor

                distance = (x_max - x_min + x_add_factor) + (y_max - y_min + y_add_factor)
                lengths_array.append(distance)
        return lengths_array
        



def part_1():
    with open('input.txt', 'r') as f:
        input_lines = f.readlines()  
    # Create a Universe
    universe = Universe(input_lines)
    # Get array of lengths
    lengths_array = universe.calculate_paths()
    return sum(lengths_array)



def part_2():
    with open('input.txt', 'r') as f:
        input_lines = f.readlines()  
    # Create a Universe
    universe = Universe(input_lines)
    # Get array of lengths
    lengths_array = universe.calculate_paths(expansion_factor=1000000)
    return sum(lengths_array)

if __name__ == '__main__':
    # print(part_1())
    print(part_2())
