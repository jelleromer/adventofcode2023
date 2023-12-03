#!/bin/python
import re

def game_is_possible(line) -> int:
    max_red, max_blue, max_green = 12, 14, 13
    y = line.split(': ')
    ID = int(re.findall(r'\d+', y[0])[0])
    x = y[1]
    red = max(map(int, re.findall(r'(\d+) red', x)))
    blue = max(map(int, re.findall(r'(\d+) blue', x)))
    green = max(map(int, re.findall(r'(\d+) green', x)))
    if red > max_red or blue > max_blue or green > max_green:
        return 0
    else:
        return ID

def power(line) -> int:
    red = max(map(int, re.findall(r'(\d+) red', line)))
    blue = max(map(int, re.findall(r'(\d+) blue', line)))
    green = max(map(int, re.findall(r'(\d+) green', line)))
    return red * blue * green

with open('input') as f:
    lines = f.read().splitlines()
    part1 = sum(map(game_is_possible, lines))
    part2 = sum(map(power, lines))
    print(part1, part2)
