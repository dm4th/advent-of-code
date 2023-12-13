import os
import sys
import time
from datetime import datetime
from typing import List, Union
import math
import concurrent.futures

def parse_schematic(schematic_str: str, mapping: List[int]):
    broken_count = sum(mapping)

def get_variations(schematic: List[str], mapping: List[int]) -> int:
    if len(schematic) == 0:
        return 0
    
    elif len(schematic) == 1:
        if len(mapping) == 1:
            return 2**(len(mapping) - mapping[0])
        else:
            return parse_schematic(schematic[0], mapping)
        
    else:
        



def calculate_variations(input_str: str) -> int:
    input_split = input_str.split(' ')
    schematic = input_split[0].split('.')
    mapping = input_split[1].split(',')

    return get_variations(schematic, mapping)


def part_1():
    with open('input-2.txt', 'r') as f:
        input_lines = f.readlines()  

    variations = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        results = [executor.submit(calculate_variations, input_str) for input_str in input_lines]

        for future in concurrent.futures.as_completed(results):
            variations.append(future.result())

    return sum(variations)

def part_2():
    with open('input.txt', 'r') as f:
        input_lines = f.readlines()  

if __name__ == '__main__':
    print(part_1())
    # print(part_2())
