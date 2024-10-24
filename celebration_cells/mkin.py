#!/usr/local/bin/python3
from random import randint, sample, choice, choices, seed
from string import ascii_lowercase
import sys
import re
case_num = int(input())
seed(case_num * 955)
# 0 and 1 are the sample cases
if case_num == 0:
    print(3)
    print(9)
elif case_num == 1:
    print(10)
    print(16)
else:
    x = randint(1, 100)
    y = randint(1, 100)
    print(x)
    print(y)
