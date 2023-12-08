#!/bin/python
import re, itertools
from functools import reduce
from typing import Callable

def directionToInt(s: str) -> int:
    match s:
        case 'L':
            return 0
        case 'R':
            return 1
        case _:
            raise ValueError

def getPathLength(startNode: str,
                  goalCondition: Callable[[str], bool],
                  indeces: list[int],
                  network: dict[str, tuple[str, str]]
                  ) -> int:
    indexGenerator = itertools.cycle(indeces)
    currentNode = startNode
    steps = 0
    while not goalCondition(currentNode):
        currentNode = network[currentNode][next(indexGenerator)]
        steps += 1
    return steps

def partone(indeces: list[int], network: dict[str, tuple[str, str]]) -> int:
    return getPathLength('AAA', lambda x: x == 'ZZZ', indeces, network)

def nodeEndsWithA(s: str) -> bool:
    return s[-1] == 'A'

def nodeEndsWithZ(s: str) -> bool:
    return s[-1] == 'Z'

def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)

def lcm(a, b):
    return (a * b) / gcd(a, b)

def parttwo(indeces: list[int], network: dict[str, tuple[str, str]]) -> int:
    lengths = [getPathLength(n, nodeEndsWithZ, indeces, network) for n in filter(nodeEndsWithA, network.keys())]
    return int(reduce(lcm, lengths, 1))

with open('input', 'r') as f:
    instructionsS, lines = f.read().split('\n\n')
    lines = lines.splitlines()
    indeces = list(map(directionToInt, instructionsS))
    network = {}
    for line in lines:
        x, y, z = re.findall(r'[A-Z]{3}', line)
        network[x] = (y, z)
    part1 = partone(indeces, network)
    part2 = parttwo(indeces, network)
    print(part1, part2)

