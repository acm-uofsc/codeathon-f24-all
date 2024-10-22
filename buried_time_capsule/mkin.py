#!/usr/local/bin/python3
from random import randint
case_num = int(input())
# 0 and 1 are the sample cases
if case_num == 0:
    print(3, 2, 5)
elif case_num == 1:
    print(3, 5, 7)
else:
    # output what should be read in as input by
    # contestant code
    a = randint(100, 10000)
    b = randint(100, 10000)
    x = randint(10000, 20000)
    print(a, b, x)
