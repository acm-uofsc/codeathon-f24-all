#!/usr/local/bin/python3
from random import randint, sample, choice, choices, seed
from string import ascii_lowercase
import sys
import re
case_num = int(input())
seed(case_num * 155)
# 0 and 1 are the sample cases
if case_num == 0:
    print(6)
    print(9)
    print(8, 3, 4, 7, 1, 5)
elif case_num == 1:
    print(8)
    print(14)
    print(12, 6, 0, 2, 41, 0, 3, 0)
else:
    x = randint(5, 1000)
    s = randint(1, 10_000)

    print(x)
    print(s)
    tiles = choices(range(1, 1000), k=x)
    #make replacements
    for i in range(randint(1, 6)):
        tiles[randint(1, len(tiles) - 1)] = 0
    print(*tiles)
