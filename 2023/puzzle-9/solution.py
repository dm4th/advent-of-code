import os
import sys
import time
from datetime import datetime
from typing import List, Union
import math
import concurrent.futures

def retrieve_differences(history: List[int]) -> Union[List[int], int]:
    if set(history) == set([0]):
        return 0
    else:
        differences = []
        for h in range(len(history)-1):
            differences.append(history[h+1] - history[h])
        return history[-1] + retrieve_differences(differences)
    
def retrieve_differences_backwards(history: List[int]) -> Union[List[int], int]:
    if set(history) == set([0]):
        return 0
    else:
        differences = []
        for h in range(len(history)-1):
            differences.append(history[h+1] - history[h])
        return history[0] - retrieve_differences_backwards(differences)

def part_1():
    with open('input.txt', 'r') as f:
        input_lines = f.readlines()  

    histories = [[int(h) for h in history.strip().split(' ')] for history in input_lines]  
    extrapolations = []

    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        results = [executor.submit(retrieve_differences, history) for history in histories]

        for future in concurrent.futures.as_completed(results):
            extrapolations.append(future.result())

    return sum(extrapolations)

def part_2():
    with open('input.txt', 'r') as f:
        input_lines = f.readlines()  

    histories = [[int(h) for h in history.strip().split(' ')] for history in input_lines]  
    extrapolations = []

    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        results = [executor.submit(retrieve_differences_backwards, history) for history in histories]

        for future in concurrent.futures.as_completed(results):
            extrapolations.append(future.result())

    return sum(extrapolations)

if __name__ == '__main__':
    # print(part_1())
    print(part_2())
