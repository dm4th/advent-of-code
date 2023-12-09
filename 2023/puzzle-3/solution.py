import os
import sys
import time

NUMS = '1234567890'
NON_SYMBOLS = NUMS + '.'

def check_neighbors(start_index, end_index, row, above, below):
    # boundary handling
    if start_index != 0:
        start = start_index - 1
    else:
        start = 0
    if end_index == len(row)-1:
        end = end_index -1
    else:
        end = end_index

    if end_index == len(row)-1:
        print('\n')
        if above:
            print(above[start:end+1])
        print(row[start:end+1])
        if below:
            print(below[start:end+1])

    # First check same row
    if row[start] not in NON_SYMBOLS:
        if end_index == len(row)-1:
            print('left')
        return True
    if row[end] not in NON_SYMBOLS:
        if end_index == len(row)-1:
            print('right', row[end])
        return True
    
    # Check above row
    if above:
        for char in above[start:end+1]:
            if char not in NON_SYMBOLS:
                if end_index == len(row)-1:
                    print('above')
                return True
    
    # Check below row
    if below:
        for char in below[start:end+1]:
            if char not in NON_SYMBOLS:
                if end_index == len(row)-1:
                    print('below')
                return True

    if end_index == len(row)-1:
        print(f'not found\tfirst: {row[start]} last: {row[end]}')
    return False

def find_part_numbers(part_rows, first=False, last=False):
    part_indices = []

    if first:
        row = part_rows[0]
        above = None
        below = part_rows[1]
    elif last:
        row = part_rows[1]
        above = part_rows[0]
        below = None
    else:
        row = part_rows[1]
        above = part_rows[0]
        below = part_rows[2]

    first_index = -1
    last_index = -1
    for i in range(len(row)):
        if first_index == -1:
            if row[i] in NUMS:
                first_index = i
        else:
            if row[i] not in NUMS or i == len(row)-1:
                last_index = i

        if first_index > -1 and last_index > -1:
            if check_neighbors(first_index, last_index, row, above, below):
                part_indices.append((first_index, last_index))
            first_index = -1
            last_index = -1

    return part_indices


def find_gear_ratios(part_rows, row, col):
    gear_nums = []

    row_len = len(part_rows[row])

    print('\n')
    if row > 0:
        print(part_rows[row-1][max(col-3,0):min(col+4,row_len-1)])
    print(part_rows[row][max(col-3,0):min(col+4,row_len-1)])
    if row < len(part_rows)-1:
        print(part_rows[row+1][max(col-3,0):min(col+4,row_len-1)])

    # check above row
    if row > 0:
        num_chars = ''
        num_flag = False
        check_row = part_rows[row-1]
        
        for c in range(max(col-3,0), min(col+4,row_len-1), 1):
            if not num_flag:
                if c > col+1:
                    break
                elif check_row[c] in NUMS:
                    num_chars = check_row[c]
                    num_flag = True

            else:
                if check_row[c] not in NUMS:
                    if c > col-1:
                        gear_nums.append(int(num_chars))
                    num_chars = ''
                    num_flag = False
                else:
                    num_chars = num_chars + check_row[c]
        if num_flag:
            gear_nums.append(int(num_chars))

    check_row = part_rows[row]
    
    # check left
    if col != 0:
        if check_row[col-1] in NUMS:
            num_chars = ''
            num_flag = False
            for c in range(col-1, max(col-4,0), -1):
                if not num_flag:
                    if check_row[c] in NUMS:
                        num_chars = num_chars + check_row[c]
                        num_flag = True

                else:
                    if check_row[c] not in NUMS:
                        gear_nums.append(int(num_chars))
                        num_chars = ''
                        num_flag = False
                    else:
                        num_chars = check_row[c] + num_chars
            if num_flag:
                gear_nums.append(int(num_chars))

    
    # check right
    if col != row_len:
        if check_row[col+1] in NUMS:
            num_chars = ''
            num_flag = False
            for c in range(col+1, min(col+4,len(check_row)-1), 1):
                if not num_flag:
                    if check_row[c] in NUMS:
                        num_chars = num_chars + check_row[c]
                        num_flag = True

                else:
                    if check_row[c] not in NUMS:
                        gear_nums.append(int(num_chars))
                        num_chars = ''
                        num_flag = False
                    else:
                        num_chars = num_chars + check_row[c]
            if num_flag:
                gear_nums.append(int(num_chars))

    # check below row
    if row < len(part_rows)-1:
        num_chars = ''
        num_flag = False
        check_row = part_rows[row+1]
        
        for c in range(max(col-3,0), min(col+4,len(check_row)-1), 1):
            if not num_flag:
                if c > col+1:
                    break
                if check_row[c] in NUMS:
                    num_chars = num_chars + check_row[c]
                    num_flag = True

            else:
                if check_row[c] not in NUMS:
                    if c > col-1:
                        gear_nums.append(int(num_chars))
                    num_chars = ''
                    num_flag = False
                else:
                    num_chars = num_chars + check_row[c]
        if num_flag:
            gear_nums.append(int(num_chars))

    print(gear_nums)

    if len(gear_nums) == 2:
        print(gear_nums[0], gear_nums[1], gear_nums[0] * gear_nums[1])
        return gear_nums[0] * gear_nums[1]
    
    else:
        return 0

            



def part_1():
    with open('input.txt', 'r') as f:
        part_rows = f.readlines()

    part_numbers = []
    for pr in range(len(part_rows)):
        if pr == 0:
            part_indices = find_part_numbers(part_rows[:pr+2], first=True)
        elif pr == len(part_rows)-1:
            part_indices = find_part_numbers(part_rows[pr-1:], last=True)
        else:
            part_indices = find_part_numbers(part_rows[pr-1:pr+2])

        for pi in part_indices:
            new_num = int(part_rows[pr][pi[0]:pi[1]])
            if pi[1] == len(part_rows[pr])-1:
                print(new_num)
            part_numbers.append(new_num)

    return sum(part_numbers)

def part_2():
    with open('input.txt', 'r') as f:
        part_rows = f.readlines()

    gear_ratios = []
    for pr in range(len(part_rows)):
        for c in range(len(part_rows[pr])):
            if part_rows[pr][c] == '*':
                gear_ratios.append(find_gear_ratios(part_rows, pr, c))
                # time.sleep(1)

    return sum(gear_ratios)

if __name__ == '__main__':
    print(part_2())