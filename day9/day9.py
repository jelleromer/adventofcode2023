#!/bin/python
import re

def parseNums(s: str) -> list[int]:
    return list(map(int, (re.findall(r'[-]?\d+', s))))

def getDifferences(ints: list[int]) -> list[int]:
    return [y - x for x, y in zip(ints[:-1], ints[1:])]

def listIsAllZeroes(ints: list[int]) -> bool:
    return all(i == 0 for i in ints)

def findNextHistoryValue(ints: list[int]) -> int:
    lists = [ints]
    while not listIsAllZeroes(lists[-1]):
        lists.append(getDifferences(lists[-1]))
    return sum(x[-1] for x in reversed(lists))

def findPreviousHistoryValue(ints: list[int]) -> int:
    lists = [ints]
    while not listIsAllZeroes(lists[-1]):
        lists.append(getDifferences(lists[-1]))
    res = 0
    for l in reversed(lists):
        res = l[0] - res
    return res

with open('input', 'r') as f:
    lines = list(map(parseNums, f.read().splitlines()))
    part1 = sum(map(findNextHistoryValue, lines))
    part2 = sum(map(findPreviousHistoryValue, lines))
    print(part1, part2)

