#!/usr/local/bin/python3
from random import randint, seed

case_num = int(input())
seed(case_num * 234)
# 0 and 1 are the sample cases
if case_num == 0:
    print('''6
4 2
3 2
4 3
5 2
2 1
3 100
4
5 3
9 5
30 5
40 6''')
elif case_num == 1:
    print('''5
9 1
4 5
3 5
4 1
2 2
2
7 5
3 3''')
else:
    # output what should be read in as input by
    # contestant code
    number_of_ingredients = randint(5, 14)
    if case_num > 10:
        number_of_ingredients = randint(50, 60)
    if case_num > 20:
        number_of_ingredients = randint(100, 1000)
    if case_num > 30:
        number_of_ingredients = randint(1400, 1500)
    print(number_of_ingredients)

    # Generate n ingredients with random weights and values
    for _ in range(number_of_ingredients):
        weight = randint(1, 50)
        value = randint(1, 10_000)
        print(weight, value)
    case_count = randint(2, 6)
    if case_num > 20:
        case_count = randint(20, 30)
    if case_num > 30:
        case_count = 15_000
    print(case_count)
    for i in range(case_count):
        max_weight_cap = randint(1, 1500)
        first_x_allowed = randint(1, number_of_ingredients)
        if case_num > 30:
            max_weight_cap = randint(1400, 1500)
            first_x_allowed = randint(number_of_ingredients-100, number_of_ingredients)
        print(max_weight_cap, first_x_allowed)

