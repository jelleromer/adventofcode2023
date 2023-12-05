#!/bin/python
import re
from typing import NamedTuple, Callable
from functools import reduce

Mapping = NamedTuple('Mapping', [('destRangeStart', int), ('sourceRangeStart', int), ('rangeLength', int)])

def mappingToFunc(mappings: list[Mapping]):
    def func(num: int) -> int:
        for m in mappings:
            n = num - m.sourceRangeStart
            if 0 <= n < m.rangeLength:
                return n + m.destRangeStart
        return num
    return func

def parseNums(s: str) -> list[int]:
    return list(map(int, (re.findall(r'\d+', s))))

def parseMappings(s: str) -> list[Mapping]:
    lines = s.splitlines()[1:]
    return [Mapping(*parseNums(x)) for x in lines]

def getFunctionComposition(funcs: list[Callable[[int], int]]) -> Callable[[int], int]:
    def fullFunc(x):
        return reduce(lambda res, func: func(res), funcs, x)
    return fullFunc

def getSeedToLocation(ss: list[str]) -> Callable[[int], int]:
    converters = list(map(mappingToFunc, map(parseMappings, ss)))
    return getFunctionComposition(converters)

def partone(ss: list[str]) -> int:
    seeds = parseNums(ss[0])
    seedToLocation = getSeedToLocation(ss[1:])
    return min(map(seedToLocation, seeds))

def parseSeedPairs(s: str) -> list[tuple[int, int]]:
    nums = parseNums(s)
    return [(nums[i], nums[i+1]) for i in range(0, len(nums), 2)]

def getIsSeed(seedPairs: list[tuple[int, int]]):
    def isSeed(i: int) -> bool:
        for start, offset in seedPairs:
            if start <= i < (start + offset):
                return True
        return False
    return isSeed

def mappingsToReversedFunc(mappings: list[Mapping]):
    def func(num: int) -> int:
        for m in mappings:
            n = num - m.destRangeStart
            if 0 <= n < m.rangeLength:
                return n + m.sourceRangeStart
        return num
    return func

def getLocationToSeed(ss: list[str]) -> Callable[[int], int]:
    converters = list(map(mappingsToReversedFunc, map(parseMappings, ss)))[::-1]
    return getFunctionComposition(converters)

def parttwo(ss: list[str]) -> int:
    isSeed = getIsSeed(parseSeedPairs(ss[0]))
    locationToSeed = getLocationToSeed(ss[1:])
    # for i in range(63179490, 63179510):
    for i in range(999999999999):
        location = locationToSeed(i)
        if isSeed(location):
            return i
    return -1

with open('input', 'r') as f:
    x = f.read().split('\n\n')
    part1 = partone(x)
    part2 = parttwo(x)
    print(part1, part2)

