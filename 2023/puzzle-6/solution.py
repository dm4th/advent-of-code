import os
import sys
from datetime import datetime
from typing import List

def calc_winners(time: int, distance: int) -> int:
    winners = 0
    for j in range(time):
        speed = j
        rem_time = time - j
        if speed*rem_time > distance:
            winners += 1
    return winners

def part_1():
    with open('input.txt', 'r') as f:
        input_lines = f.readlines()

    time_row = input_lines[0].strip().split(' ') 
    distance_row = input_lines[1].strip().split(' ') 

    times = []
    distances = []

    for t in time_row:
        try:
            times.append(int(t))
        except:
            pass
    for d in distance_row:
        try:
            distances.append(int(d))
        except:
            pass

    winnings = []
    for i in range(len(times)):
        winnings.append(calc_winners(times[i], distances[i]))

    combos = 1
    for w in winnings:
        combos *= w

    return combos

def part_2():
    with open('input.txt', 'r') as f:
        input_lines = f.readlines()

    time = int(input_lines[0].strip().replace('Time:','').replace(' ',''))
    distance = int(input_lines[1].strip().replace('Distance:','').replace(' ','')) 

    return calc_winners(time, distance)

if __name__ == '__main__':
    # print(part_1())
    print(part_2())