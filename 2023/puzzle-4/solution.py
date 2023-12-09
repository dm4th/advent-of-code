import os
import sys
import time

def get_card_winnings(card):
    name_split = card.split(':')
    card_number = name_split[0]
    values = name_split[1]

    values_split = values.split('|')
    nums_str = values_split[0].replace('\n','')
    winning_nums_str = values_split[1].replace('\n','')

    nums_temp = nums_str.split(' ')
    winning_nums_temp = winning_nums_str.split(' ')

    winning_nums = []
    for winning_num in winning_nums_temp:
        try:
            winning_nums.append(int(winning_num))
        except ValueError:
            pass

    nums = []
    for num in nums_temp:
        try:
            nums.append(int(num))
        except ValueError:
            pass

    power = -1
    print(f'\n\n{card_number}')
    for num in nums:
        if num in winning_nums and num != '':
            print(f'\t{num} found in {winning_nums}')
            power+=1

    if power == -1:
        output = 0
    else:
        output = 2**power
    print(f'Power: {power}, Output: {output}')
    return output

def get_copy_counts(card, copies):
    name_split = card.split(':')
    card_number_str = name_split[0]
    card_number = int(card_number_str.replace('Card','').strip())

    values = name_split[1]
    values_split = values.split('|')
    nums_str = values_split[0].replace('\n','')
    winning_nums_str = values_split[1].replace('\n','')

    nums_temp = nums_str.split(' ')
    winning_nums_temp = winning_nums_str.split(' ')

    winning_nums = []
    for winning_num in winning_nums_temp:
        try:
            winning_nums.append(int(winning_num))
        except ValueError:
            pass

    nums = []
    for num in nums_temp:
        try:
            nums.append(int(num))
        except ValueError:
            pass

    # First get a count of this card's winners
    winners = 0
    for num in nums:
        if num in winning_nums:
            winners += 1

    # Next get how many copies you'll need to make
    copy_count = 1
    for copy in copies:
        if copy == card_number:
            copy_count += 1

    # Create the array of copies we'll extend copies by
    if winners != 0:
        added_copies = list(range(card_number+1, card_number+1+winners))*copy_count
        copies.extend(added_copies)

    return copies


def part_1():
    with open('input.txt', 'r') as f:
        cards = f.readlines()

    card_values = []
    for card in cards:
        card_values.append(get_card_winnings(card))

    return sum(card_values)

def part_2():
    with open('input.txt', 'r') as f:
        cards = f.readlines()

    copies = []
    for card in cards:
        new_copies = get_copy_counts(card, copies)
        copies = new_copies

    return len(copies) + len(cards)


if __name__ == '__main__':
    # print(part_1())
    print(part_2())