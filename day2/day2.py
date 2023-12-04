#!/bin/python
import re
from functools import reduce, partial
from operator import mul

def getCubes(color: str, line: str) -> int:
    regex = r'(\d+) '
    return max(map(int, re.findall(f'{regex}{color}', line)))

def game_is_possible(line: str) -> int:
    y = line.split(': ')
    ID = int(re.findall(r'\d+', y[0])[0])
    x = y[1]
    maximums = [('red', 12), ('green', 13), ('blue', 14)]
    if any(getCubes(color, x) > m for color, m in maximums):
        return 0
    else:
        return ID

def power(line: str) -> int:
    return reduce(mul, map(partial(getCubes, line=line), ['red', 'green', 'blue']))

with open('input', 'r') as f:
    lines = f.read().splitlines()
    part1 = sum(map(game_is_possible, lines))
    part2 = sum(map(power, lines))
    print(part1, part2)
