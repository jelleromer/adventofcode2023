#!/bin/python
import re
from operator import mul
from functools import reduce

def findNumLocations(lines: list[str]) -> list[tuple[int, int, int, int]]:
    res = []
    for y, line in enumerate(lines):
        matches = re.finditer(r'\d+', line)
        for match in matches:
            res.append((y, match.start(), match.end()-1, int(match.group())))
    return res

def isSymbol(s: str) -> bool:
    return s in '*-@%=$+#&/'

def isPartNumber(lines: list[str], y: int, x1: int, x2: int) -> bool:
    maxX = len(lines[0]) - 1
    if x1 != 0:
        x1 = x1 - 1
    if x2 != maxX:
        x2 = x2 + 1
    # scan line above
    if y != 0:
        for i in range(x1, x2+1):
            if isSymbol(lines[y-1][i]):
                return True
    # scan line below
    if y != len(lines)-1:
        for i in range(x1, x2+1):
            if isSymbol(lines[y+1][i]):
                return True
    # scan sides
    if isSymbol(lines[y][x1]) or isSymbol(lines[y][x2]):
        return True
    return False

def partone(lines: list[str]):
    return sum(loc[3] for loc in findNumLocations(lines) if isPartNumber(lines, *loc[:3]))

def findGearLocations(lines: list[str]) -> list[tuple[int, int]]:
    res = []
    for y, line in enumerate(lines):
        matches = re.finditer(r'\*', line)
        for match in matches:
            res.append((match.start(), y))
    return res

def isSurroundingGear(gearLoc: tuple[int, int], x: int, y: int) -> bool:
    xg, yg = gearLoc
    return xg-1 <= x <= xg+1 and yg-1 <= y <= yg+1

def getSurroundingNumbers(lines: list[str], gearLoc: tuple[int, int]) -> list[int]:
    res = []
    _, y = gearLoc
    linesToCheck = list(enumerate(lines))[y-1 if y!=0 else y : y+2 if y!=len(lines)-1 else y+1]
    for j, line in linesToCheck:
        matches = re.finditer(r'\d+', line)
        for match in matches:
            for i in range(match.start(), match.end()):
                if isSurroundingGear(gearLoc, i, j):
                    res.append(int(match.group()))
                    break
    return res

def parttwo(lines: list[str]):
    res = 0
    for gearLoc in findGearLocations(lines):
        nums = getSurroundingNumbers(lines, gearLoc)
        if len(nums) == 2:
            res += reduce(mul, nums)
    return res

with open('input', 'r') as f:
    lines = f.read().splitlines()
    part1 = partone(lines)
    part2 = parttwo(lines)
    print(part1, part2)

