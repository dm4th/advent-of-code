import os
import sys
from datetime import datetime
from typing import List

CARD_VALUES = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}

CARD_VALUES_J = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 1,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}

def cards_gt(a: str, b: str, joker: bool = False) -> bool:
    if joker:
        return CARD_VALUES_J[a] > CARD_VALUES_J[b]
    return CARD_VALUES[a] > CARD_VALUES[b]

def cards_gte(a: str, b: str, joker: bool = False) -> bool:
    if joker:
        return CARD_VALUES_J[a] >= CARD_VALUES_J[b]
    return CARD_VALUES[a] >= CARD_VALUES[b]

def cards_lt(a: str, b: str, joker: bool = False) -> bool:
    if joker:
        return CARD_VALUES_J[a] < CARD_VALUES_J[b]
    return CARD_VALUES[a] < CARD_VALUES[b]

def cards_lte(a: str, b: str, joker: bool = False) -> bool:
    if joker:
        return CARD_VALUES_J[a] <= CARD_VALUES_J[b]
    return CARD_VALUES[a] <= CARD_VALUES[b]

def cards_eq(a: str, b: str, joker: bool = False) -> bool:
    if joker:
        return CARD_VALUES_J[a] == CARD_VALUES_J[b]
    return CARD_VALUES[a] == CARD_VALUES[b]

def cards_ne(a: str, b: str, joker: bool = False) -> bool:
    if joker:
        return CARD_VALUES_J[a] != CARD_VALUES_J[b]
    return CARD_VALUES[a] != CARD_VALUES[b]

class Hand:

    def __init__(self, hand_str: str, bid_str: str) -> None:
        self.hand = hand_str
        self.bid = int(bid_str)
        self.hand_dict = {}
        
        for card in self.hand:
            if card in self.hand_dict.keys():
                self.hand_dict[card] += 1
            else:
                self.hand_dict[card] = 1

        vals = self.hand_dict.values()
        if 5 in vals:
            self.type = 6
        elif 4 in vals:
            self.type = 5
        elif 3 in vals:
            if 2 in vals:
                self.type = 4
            else:
                self.type = 3
        elif 2 in vals:
            if len(self.hand_dict.keys()) == 3:
                self.type = 2
            else:
                self.type = 1
        else:
            self.type = 0

    def __repr__(self) -> str:
        return f'{self.hand} - {self.type}'

    def __str__(self) -> str:
        return f'{self.hand} - {self.type}'
    
    def __gt__(self, other: 'Hand') -> bool:
        if self.type == other.type:
            for c in range(len(self.hand)):
                if cards_gt(self.hand[c], other.hand[c]):
                    return True
            return False
        else:
            return self.type > other.type

    def __lt__(self, other: 'Hand') -> bool:
        if self.type == other.type:
            for c in range(len(self.hand)):
                if self.hand[c] != other.hand[c]:
                    return cards_lt(self.hand[c], other.hand[c])
            return False
        else:
            return self.type < other.type

    def __eq__(self, other: 'Hand') -> bool:
        return self.hand == other.hand
        

class JokerHand(Hand):

    def __init__(self, hand_str: str, bid_str: str) -> None:
        super().__init__(hand_str, bid_str)

        if 'J' in self.hand_dict.keys():
            jokers = self.hand_dict['J']
        else:
            jokers = 0

        # 6 = 5 of a kind
        # 5 = 4 of a kind
        # 4 = full house
        # 3 = 3 of a kind
        # 2 = 2 pair
        # 1 = 1 pair
        # 0 = high card
        if jokers > 0:
            if self.type == 5:
                # print(f'{self.hand}:\t4 of a kind --> 5 of a kind\t{self.type} --> 6')
                self.type = 6
            elif self.type == 4:
                # print(f'{self.hand}:\tFull House --> 5 of a kind\t{self.type} --> 6')
                self.type = 6
            elif self.type == 3:
                # print(f'{self.hand}:\t3 of a kind --> 4 of a kind\t{self.type} --> 5')
                self.type = 5
            elif self.type == 2:
                if jokers == 2:
                    # print(f'{self.hand}:\t2 Pair --> 4 of a kind\t{self.type} --> 5')
                    self.type = 5
                elif jokers == 1:
                    # print(f'{self.hand}:\t2 Pair --> Full House\t{self.type} --> 4')
                    self.type = 4
            elif self.type == 1 and jokers > 0:
                # print(f'{self.hand}:\t1 Pair --> 3 of a kind\t{self.type} --> 3')
                self.type = 3
            elif self.type == 0 and jokers == 1:
                # print(f'{self.hand}:\tHigh Card --> 1 Pair\t{self.type} --> 1')
                self.type = 1
            else:
                print(f'{self.hand}:\tJoker with No Change\t{self.type}')
    
    def __gt__(self, other: 'Hand') -> bool:
        if self.type == other.type:
            for c in range(len(self.hand)):
                if self.hand[c] != other.hand[c]:
                    return cards_gt(self.hand[c], other.hand[c], joker=True)
            return False
        else:
            return self.type > other.type

    def __lt__(self, other: 'Hand') -> bool:
        if self.type == other.type:
            for c in range(len(self.hand)):
                if self.hand[c] != other.hand[c]:
                    return cards_lt(self.hand[c], other.hand[c], joker=True)
            return False
        else:
            return self.type < other.type
        





def part_1():
    with open('input.txt', 'r') as f:
        input_lines = f.readlines()

    hands = []
    for line in input_lines:
        line_vals = line.split(' ')
        hands.append(Hand(line_vals[0], line_vals[1]))

    hands.sort()

    winnings = 0
    for h in range(len(hands)):
        winnings += hands[h].bid * (h+1)

    return winnings

def part_2():
    with open('input.txt', 'r') as f:
        input_lines = f.readlines()

    hands = []
    for line in input_lines:
        line_vals = line.split(' ')
        hands.append(JokerHand(line_vals[0], line_vals[1]))

    hands.sort()

    winnings = 0
    for h in range(len(hands)):
        winnings += hands[h].bid * (h+1)

    return winnings

if __name__ == '__main__':
    # print(part_1())
    print(part_2())