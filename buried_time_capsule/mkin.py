#!/usr/local/bin/python3
from random import randint
case_num = int(input())
# 0 and 1 are the sample cases
if case_num == 0:
    print(2)
    print(3, 2, 5)
    print(10, 2, 5)
elif case_num == 1:
    print(1)
    print(2, 5, 1)
else:
    # output what should be read in as input by
    # contestant code
    case_count = randint(2, 4)
    is_hard_case = case_num > 15
    if is_hard_case:
        case_count = 20
    print(case_count)
    for i in range(case_count):
        if is_hard_case:
            a = randint(1, 10000)
            b = randint(1, 10000)
            x = randint(1, 20000)
        else:
            a = randint(1, 4)
            b = randint(1, 10)
            x = -randint(0,2)*a + randint(0,2)*b
            while x <= 0:
                x += b
        if case_num == 40:
            a = randint(1, 10)
            b = randint(1, 3)
            x = randint(20000-15, 20000)
        print(a, b, x)
