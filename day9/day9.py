#!/bin/python
import re
from functools import reduce

def parseNums(s: str) -> list[int]:
    return list(map(int, (re.findall(r'[-]?\d+', s))))

def getDifferences(ints: list[int]) -> list[int]:
    return [y - x for x, y in zip(ints[:-1], ints[1:])]

def listIsAllZeroes(ints: list[int]) -> bool:
    return all(i == 0 for i in ints)

def generateHistory(ints: list[int]) -> list[list[int]]:
    if listIsAllZeroes(ints):
        return [ints]
    return [ints] + generateHistory(getDifferences(ints))

def findNextHistoryValue(ints: list[int]) -> int:
    return sum(h[-1] for h in reversed(generateHistory(ints)))

def findPreviousHistoryValue(ints: list[int]) -> int:
    leftMosts = [h[0] for h in reversed(generateHistory(ints))]
    return reduce(lambda x, y: y - x, leftMosts, 0)

with open('input', 'r') as f:
    lines = list(map(parseNums, f.read().splitlines()))
    part1 = sum(map(findNextHistoryValue, lines))
    part2 = sum(map(findPreviousHistoryValue, lines))
    print(part1, part2)

