#!/bin/python
import re
from typing import NamedTuple
from functools import reduce
from operator import mul

Record = NamedTuple('Record', [('time', int), ('wr_distance', int)])

def parseNums(s: str) -> list[int]:
    return list(map(int, (re.findall(r'\d+', s))))

def parseRecords(ss: list[str]) -> list[Record]:
    return [Record(*x) for x in zip(*map(parseNums, ss))]

def numberOfWaysToWin(r: Record) -> int:
    speed = 0
    res = []
    for i in range(r.time):
        speed = i
        timeLeft = r.time - i
        distance = speed * timeLeft
        res.append(distance > r.wr_distance)
    return sum(map(int, res))

def parseOneBigNum(s: str) -> list[int]:
    s = re.sub(r'\s', '', s)
    return list(map(int, (re.findall(r'\d+', s))))

def parseOneBigRecord(ss: list[str]) -> list[Record]:
    return [Record(*x) for x in zip(*map(parseOneBigNum, ss))]

with open('input', 'r') as f:
    lines = f.read().splitlines()
    records = parseRecords(lines)
    y = numberOfWaysToWin(records[0])
    part1 = reduce(mul, map(numberOfWaysToWin, records))
    z = parseOneBigRecord(lines)[0]
    part2 = numberOfWaysToWin(z)
    print(part1, part2)

