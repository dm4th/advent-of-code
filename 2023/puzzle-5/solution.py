import os
import sys
from datetime import datetime
from typing import List

def print_progress_bar(progress: int, total: int) -> str:
    percent = round(progress / total * 100, 1)
    bar = '#' * int(percent / 2)
    return f'{percent}% [{bar:50}] {progress}/{total}'


class MappingRange:

    def __init__(self, range_list: List[str]) -> None:
        self.destination_start = int(range_list[0].strip())
        self.source_start = int(range_list[1].strip())
        self.range_length = int(range_list[2].strip())
        self.destination_end = self.destination_start + self.range_length
        self.source_end = self.source_start + self.range_length

    def find_destination_value(self, value: int) -> int or None:
        if value >= self.source_start and value <= self.source_end:
            return self.destination_start + (value - self.source_start)
        else:
            return None
        
    def find_source_value(self, value: int) -> int or None:
        if value >= self.destination_start and value < self.destination_end:
            return self.source_start + (value - self.destination_start)
        else:
            return None

class Mapping:

    def __init__(self, name_str: str) -> None:
        name_list = name_str.split('-to-')
        self.source = name_list[0]
        self.destination = name_list[1]
        self.mappings = []

    def __repr__(self) -> str:
        return f'{self.source}-to-{self.destination}: {len(self.mappings)}'

    def __str__(self) -> str:
        return f'{self.source}-to-{self.destination}: {len(self.mappings)}'
    
    def add_mapping_range(self, range_str: str or None) -> None:
        if range_str:
            self.mappings.append(MappingRange(range_str))

    def find_destination(self, value: int) -> int:
        for mapping in self.mappings:
            ret_val = mapping.find_destination_value(value)
            if ret_val:
                return ret_val
        return value
    
    def find_source(self, value: int) -> int:
        for mapping_range in self.mappings:
            ret_val = mapping_range.find_source_value(value)
            if ret_val:
                return ret_val
        return value



class MappingContainer:

    def __init__(self) -> None:
        self.mappings = []

    def __repr__(self) -> str:
        return_str = f'Mapping Container:\n'
        for m in self.mappings:
            return_str += str(m)
        return return_str

    def add_mapping(self, mapping: Mapping or None) -> None:
        if mapping:
            self.mappings.append(mapping)

    def find_mapping(self, source_str: str) -> str or None:
        for map in self.mappings:
            if map.source == source_str:
                return map
        return None

    def find_mapping_by_dest(self, dest_str: str) -> str or None:
        for map in self.mappings:
            if map.destination == dest_str:
                return map
        return None

    def find_destination_with_source(self, source: str, value: int) -> int or None:
        map = self.find_mapping(source)
        if map:
            return map.find_destination(value), map.destination

    def find_source_with_destination(self, dest: str, value: int) -> int or None:
        map = self.find_mapping_by_dest(dest)
        if map:
            return map.find_source(value), map.source
        else:
            raise ValueError
        

        

def part_1():
    with open('input.txt', 'r') as f:
        input_text = f.readlines()

    seeds_str = input_text[0].replace('seeds: ', '').replace('\n', '')
    seeds = seeds_str.split(' ')
    seeds = [int(seed) for seed in seeds]

    mappings_container = MappingContainer()

    for row in input_text[2:]:
        row_list = row.split(' ')
        if 'map' in row:
            current_map = Mapping(row_list[0])
        elif len(row_list) == 3:
            current_map.add_mapping_range(row_list)
        else:
            print(f'Adding:\t{current_map}')
            mappings_container.add_mapping(current_map)
            current_map = None

    print(f'Adding:\t{current_map}')
    mappings_container.add_mapping(current_map)

    locations = []
    for seed in seeds:
        next_source = 'seed'
        next_val = seed
        while next_source != 'location':
            next_val, next_source = mappings_container.find_destination_with_source(next_source, next_val)
        locations.append(next_val)

    return min(locations)


def part_2():
    with open('input.txt', 'r') as f:
        input_text = f.readlines()

    mappings_container = MappingContainer()

    for row in input_text[2:]:
        row_list = row.split(' ')
        if 'map' in row:
            current_map = Mapping(row_list[0])
        elif len(row_list) == 3:
            current_map.add_mapping_range(row_list)
        else:
            print(f'Adding:\t{current_map}')
            mappings_container.add_mapping(current_map)
            current_map = None

    print(f'Adding:\t{current_map}')
    mappings_container.add_mapping(current_map)

    seeds_str = input_text[0].replace('seeds: ', '').replace('\n', '')
    seeds_list = seeds_str.split(' ')
    seeds_list = [int(sl) for sl in seeds_list]
    print(seeds_list)

    seed_ranges = []
    for sl in range(len(seeds_list)):
        if sl % 2 == 1:
            start = seeds_list[sl-1]
            range_len = seeds_list[sl]
            seed_ranges.append((start, start+range_len))
    print(seed_ranges)

    min_location = False
    check_val = 0
    while not min_location:
        # print(f'\n\nCheck Val: {check_val}')
        next_val = check_val
        next_dest = 'location'
        while next_dest != 'seed':
            # print(f'\tNext Val: {next_val}')
            next_val, next_dest = mappings_container.find_source_with_destination(next_dest, next_val)
        # print(f'\tChecking {next_val}')
        for sr in seed_ranges:
            if next_val >= sr[0] and next_val <= sr[1]:
                # print(f'\n\nFound {next_val} between {sr[0]} and {sr[1]} -> {check_val}')
                min_location = True
        check_val += 1

    return check_val-1


if __name__ == '__main__':
    # print(part_1())
    print(part_2())