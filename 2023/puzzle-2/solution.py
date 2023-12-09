import sys
import os

def is_possible_1(game, bag):
    game_split = game.split(':')
    game_id_text = game_split[0].replace(':', '')
    rounds_text = game_split[1].replace(':', '').strip()

    game_id = int(game_id_text.split(' ')[1].strip())

    rounds = rounds_text.split(';')
    for round in rounds:
        cubes = round.split(',')

        for cube in cubes:

            if 'red' in cube:
                color = 'red'

            elif 'green' in cube:
                color = 'green'

            elif 'blue' in cube:
                color = 'blue'

            else:
                raise Exception
            
            blocks = int(cube.replace(color, ''))
            if blocks > bag[color]:
                return (game_id, False)
            
    return (game_id, True)

def power(game):
    game_split = game.split(':')
    rounds_text = game_split[1].replace(':', '').strip()

    rounds = rounds_text.split(';')
    minimums = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for round in rounds:
        cubes = round.split(',')

        for cube in cubes:

            if 'red' in cube:
                color = 'red'

            elif 'green' in cube:
                color = 'green'

            elif 'blue' in cube:
                color = 'blue'

            else:
                raise Exception
            
            blocks = int(cube.replace(color, ''))
            minimums[color] = max(minimums[color], blocks)
            
    return minimums['red'] * minimums['green'] * minimums['blue']

def main_1():
    BAG = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    with open('input.txt', 'r') as f:
        games = f.readlines()

    possible = []
    for game in games:
        possible_result = is_possible_1(game, BAG)
        if possible_result[1]:
            possible.append(possible_result[0])

    return sum(possible)

def main_2():

    with open('input.txt', 'r') as f:
        games = f.readlines()

    powers = []
    for game in games:
        powers.append(power(game))

    return sum(powers)

if __name__ == '__main__':
    print(main_2())