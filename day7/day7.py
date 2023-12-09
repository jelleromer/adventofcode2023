#!/bin/python
from collections import Counter

T = {
    'FiveOfAKind': 7,
    'FourOfAKind': 6,
    'FullHouse': 5,
    'ThreeOfAKind': 4,
    'TwoPair': 3,
    'OnePair': 2,
    'HighCard': 1,
    }

def cardsToType(cards: list[str], joker: bool) -> int:
    cardCounts = sorted(Counter(cards).values())
    if joker:
        amount_jokers = cards.count('J')
        if 0 < amount_jokers < 5:
            cardCounts.remove(amount_jokers)
            cardCounts[-1] += amount_jokers
    match cardCounts:
        case [5]:
            return T['FiveOfAKind']
        case [1, 4]:
            return T['FourOfAKind']
        case [2, 3]:
            return T['FullHouse']
        case [1, 1, 3]:
            return T['ThreeOfAKind']
        case [1, 2, 2]:
            return T['TwoPair']
        case [1, 1, 1, 2]:
            return T['OnePair']
        case [1, 1, 1, 1, 1]:
            return T['HighCard']
        case _:
            raise ValueError

def parseHand(s: str, joker: bool):
    hand, bid = s.split()
    cards = list(hand)
    handType = cardsToType(cards, joker)
    order = 'J23456789TQKA' if joker else '23456789TJQKA'
    cardValues = [order.index(c) for c in cards]
    return (handType, cardValues, int(bid))

def solve(lines: list[str], joker: bool):
    hands = [parseHand(l, joker) for l in lines]
    return sum([(i+1) * h[2] for i, h in enumerate(sorted(hands))])

with open('input', 'r') as f:
    lines = f.read().splitlines()
    part1 = solve(lines, False)
    part2 = solve(lines, True)
    print(part1, part2)

