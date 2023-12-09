import os
import sys
import time
from datetime import datetime
from typing import List
import math
import concurrent.futures

def check_for_z(check_list: List[str]) -> int:
    # print(f'Checking: {check_list} --> {len([s for s in check_list if s[-1] == "Z"])}')
    # time.sleep(2)
    return len([s for s in check_list if s[-1] == 'Z'])

def find_z_steps(start_node: str, directions: str, mappings: dict) -> int:
    step_count = 0
    rl_index = 0
    while start_node[-1] != 'Z':
        step_count += 1
        if rl_index == len(directions):
            rl_index = 0
        # print(f'Start Node: {start_node}, Direction: {directions[rl_index]}, Mapping: {mappings[start_node]} -> {mappings[start_node][directions[rl_index]]}')
        # time.sleep(3)
        start_node = mappings[start_node][directions[rl_index]]
        rl_index+=1
    return step_count


def part_1():
    with open('input.txt', 'r') as f:
        input_lines = f.readlines()

    directions = input_lines[0].strip()

    mappings = {}
    for mapping in input_lines[2:]:
        mapping = mapping.replace(' ', '').replace('(', '').replace(')', '').strip()
        mapping_split = mapping.split('=')
        mapping_key = mapping_split[0]
        mapping_values = mapping_split[1]
        mapping_values_split = mapping_values.split(',')
        left = mapping_values_split[0]
        right = mapping_values_split[1]
        mappings[mapping_key] = {'L': left, 'R': right}

    step_count = 0
    current_step = 'AAA'
    while current_step != 'ZZZ':
        for d in directions:
            step_count += 1
            current_step = mappings[current_step][d]
            if current_step == 'ZZZ':
                return step_count

    return step_count

def part_2():
    with open('input.txt', 'r') as f:
        input_lines = f.readlines()

    directions = input_lines[0].strip()

    mappings = {}
    for mapping in input_lines[2:]:
        mapping = mapping.replace(' ', '').replace('(', '').replace(')', '').strip()
        mapping_split = mapping.split('=')
        mapping_key = mapping_split[0]
        mapping_values = mapping_split[1]
        mapping_values_split = mapping_values.split(',')
        left = mapping_values_split[0]
        right = mapping_values_split[1]
        mappings[mapping_key] = {'L': left, 'R': right}

    nodes = [n for n in mappings.keys() if n[-1] == 'A']
    print(nodes)
    node_z_count = []
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=len(nodes)) as executor:
        results = [executor.submit(find_z_steps, n, directions, mappings) for n in nodes]

        for future in concurrent.futures.as_completed(results):
            node_z_count.append(future.result())

    return math.lcm(*node_z_count)

if __name__ == '__main__':
    # print(part_1())
    print(part_2())
