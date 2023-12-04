#!/bin/python
import re
from typing import Callable

def solve(lines: list[str], func: Callable[[str], int], regex: str) -> int:
    def lineToInt(s: str) -> int:
        xs = list(map(func, re.findall(regex, s)))
        return xs[0] * 10 + xs[-1]
    return sum(map(lineToInt, lines))

def wordToNum(s: str) -> int:
    try:
        return int(s)
    except ValueError:
        nums = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9 }
        return nums[s]

with open('input', 'r') as f:
    lines = f.read().splitlines()
    part1 = solve(lines, int, r'\d')
    part2 = solve(lines, wordToNum, r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))')
    print(part1, part2)
