#!/bin/python
import re, math

def parseNums(line: str) -> list[int]:
    return list(map(int, re.findall(r'\d+', line)))

def getWinningNums(line: str) -> int:
    winningS, mineS = line.split(': ')[1].split('|')
    winning = parseNums(winningS)
    mine = parseNums(mineS)
    return sum([int(n in mine) for n in winning])

def partone(line: str) -> int:
    power = getWinningNums(line) - 1
    if power == -1:
        return 0
    else:
        return int(math.pow(2, power))

def parttwo(lines: list[str]):
    cards = list(enumerate([getWinningNums(x) for x in lines]))
    amounts = [1 for _ in cards]
    for i in range(len(cards)):
        for _ in range(amounts[cards[i][0]]):
            for j in range(cards[i][1]):
                idx = cards[i][0] + j + 1
                amounts[idx] += 1
    return sum(amounts)

with open('input') as f:
    lines = f.read().splitlines()
    part1 = sum(map(partone, lines))
    part2 = parttwo(lines)
    print(part1, part2)
