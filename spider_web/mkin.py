#!/usr/local/bin/python3
from random import randint, sample, choice, choices, seed
from string import ascii_lowercase
import sys
import re
case_num = int(input())
seed(case_num * 555)
# 0 and 1 are the sample cases
if case_num == 0:
    print(3)
    print(4, 8)
    print(6, 1, 0, 4)
    print(3, 5)
    print(4, 8)
    print(7, 3, 0, 4)
    print(3, 12)
    print(4, 8)
    print(7, 3, 0, 4)
    print(3000, 12)
else:
    # output what should be read in as input by
    # contestant code
    is_hard_case = case_num > 35
    case_count = 8
    if is_hard_case:
        case_count = (case_num % 2) + 1
    print(case_count)
    for t in range(case_count):
        if case_num < 20:
            L = randint(1, case_num * 2)
            S = randint(1, case_num * 2)
        else:
            if is_hard_case:
                L = 200_000 // case_count
                S = 200_000 // case_count
            else:
                L = randint(case_num * 100, 20_000)
                S = randint(case_num * 100, 20_000)
        x = randint(0, S-1)
        a = randint(0, S-1)
        y = randint(1, L)
        b = randint(1, L)
        d = randint(0, 1_000)
        r = randint(0, 1_000)
        print(L, S)
        print(x, y, a, b)
        print(d, r)
