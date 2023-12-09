import sys
import os

def is_number(s):
    try:
        _ = int(s)
        return True
    except:
        return False

def get_char_num(chars):
    num_vals = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    print(f'\t{chars}')
    if len(chars) >= 5:
        if chars[:5] in num_vals.keys():
            return num_vals[chars[:5]]
    if len(chars) >= 4:
        if chars[:4] in num_vals.keys():
            return num_vals[chars[:4]]
    if len(chars) >= 3:
        if chars[:3] in num_vals.keys():
            return num_vals[chars[:3]]
        
    return None

    
def get_line_value(line):
    for c in range(len(line)):
        if is_number(line[c]):
            first_num = line[c]
            break
        first_num = get_char_num(line[c:])
        if first_num:
            break

    for c in range(len(line))[::-1]:
        if is_number(line[c]):
            last_num = line[c]
            break
        last_num = get_char_num(line[c:])
        if last_num:
            break

    return int(first_num + last_num)

def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()

    line_values = []
    for line in lines:
        line_values.append(get_line_value(line))

    return sum(line_values)

if __name__ == '__main__':
    print(main())
        