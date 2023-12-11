import os
import sys
import time
from datetime import datetime
from typing import List, Union
import math
import concurrent.futures

class Universe:

    def __init__(self, universe_rows: List[str]) -> None:

        # Expand Universe at init time
        new_universe = []
        column_planet_counts = [0] * len(universe_rows[0])
        for r in range(len(universe_rows)):
            row_planet_count = 0
            row = universe_rows[r]
            for i in range(len(row)):
                if row[i] == '#':
                    column_planet_counts[i] += 1
                    row_planet_count += 1
            
            # If the row had no planets, add it to the new universe twice to expand
            if row_planet_count == 0:
                new_universe.append(row)
            new_universe.append(row)
        
        for c in range(len(column_planet_counts)):
            # If the column had no plants , expand every row at that point with a period
            if column_planet_counts == 0:
                for r in range(len(new_universe)):
                    new_universe[r] = new_universe[r][:c] + '.' + new_universe[r][c:]

        self.universe = new_universe
        self.planets = []

        # Add array of planet coordinates
        for y in range(len(self.universe)):
            for x in range(len(self.universe[y])):
                if self.universe[y][x] == '#':
                    self.planets.append((x, y))

    def calculate_paths(self) -> List[int]:
        lengths_array = []
        for p in range(len(self.planets)-1):
            for o in range(len(self.planets[p:])):
                planet_p = self.planets[p]
                planet_o = self.planets[o]
                distance = abs(planet_p[0]-planet_o[0]) + abs(planet_p[1]-planet_o[1])
                # print(f'Checking {planet_p} vs. {planet_o}:\t{distance}')
                lengths_array.append(distance+1)
        return lengths_array
        



def part_1():
    with open('input.txt', 'r') as f:
        input_lines = f.readlines()  

    # Create a Universe
    universe = Universe(input_lines)

    print(universe.planets)

    # Get array of lengths
    lengths_array = universe.calculate_paths()

    return sum(lengths_array)



def part_2():
    with open('input.txt', 'r') as f:
        input_lines = f.readlines()  

if __name__ == '__main__':
    print(part_1())
    # print(part_2())
