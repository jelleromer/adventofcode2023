#!/bin/python
import re, math
from typing import NamedTuple

Card = NamedTuple('Card', [('index', int), ('wins', int)])

def parseNums(s: str) -> list[int]:
    return list(map(int, re.findall(r'\d+', s)))

def getAmountOfWinningNums(line: str) -> int:
    winning, mine = map(parseNums, line.split(': ')[1].split('|'))
    return sum(int(n in mine) for n in winning)

def cardToPoints(line: str) -> int:
    exponent = getAmountOfWinningNums(line) - 1
    return 0 if exponent == -1 else int(math.pow(2, exponent))

def getAmountOfScratchcards(lines: list[str]):
    cards = [Card(*x) for x in enumerate(map(getAmountOfWinningNums, lines))]
    amounts = [1] * len(cards)
    for card in cards:
        for i in range(card.wins):
            index = card.index + i + 1
            amounts[index] += amounts[card.index]
    return sum(amounts)

with open('input', 'r') as f:
    lines = f.read().splitlines()
    part1 = sum(map(cardToPoints, lines))
    part2 = getAmountOfScratchcards(lines)
    print(part1, part2)
