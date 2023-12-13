import os
import sys
import time
from datetime import datetime
from typing import List, Union
import math
import concurrent.futures

def count_char(input_str: str, char_list: List[str]) -> int:
    ret_val = 0
    for s in input_str:
        if s in char_list:
            ret_val += 1
    return ret_val

def get_char_indices(input_str: str, char: str) -> List[int]:
    ret_val = []
    for s in range(len(input_str)):
        if input_str[s] == char:
            ret_val.append(s)
    return ret_val

def count_scenarios(schematic_str: str, mapping_int: int) -> int:
    iterations = 2**count_char(schematic_str,['?'])
    ret_val = 0
    while iterations > 0:
        return 0


    

def parse_schematic(schematic_str: str, mapping: List[int]) -> int:
    pass
    

def get_variations(schematic: List[str], mapping: List[int]) -> int:
    if len(schematic) == 0:
        return 0
    
    elif len(schematic) == 1:
        if len(mapping) == 1:
            return count_scenarios(schematic[0], mapping[0])
        else:
            return parse_schematic(schematic[0], mapping)
        
    else:
        # get the potential number of broken pieces in the first schematic
        schematic_0 = schematic.pop(0)
        potential_broken = count_char(schematic_0, ['?','#'])
        if potential_broken == mapping[0]:
            return 0


        



def calculate_variations(input_str: str) -> int:
    input_split = input_str.split(' ')
    schematic = input_split[0].split('.')
    mapping = input_split[1].split(',')
    mapping = [int(m) for m in mapping]

    print(schematic, mapping)

    return get_variations(schematic, mapping)


def part_1():
    with open('input-2.txt', 'r') as f:
        input_lines = f.readlines()  

    variations = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        results = [executor.submit(calculate_variations, input_str.strip()) for input_str in input_lines]

        for future in concurrent.futures.as_completed(results):
            variations.append(future.result())

    return sum(variations)

def part_2():
    with open('input.txt', 'r') as f:
        input_lines = f.readlines()  

if __name__ == '__main__':
    print(part_1())
    # print(part_2())
