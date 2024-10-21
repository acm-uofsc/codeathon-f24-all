#!/usr/local/bin/python3
from random import randint

case_num = int(input())
# 0 and 1 are the sample cases
if case_num == 0:
    target_weight = randint(10, 20)
    number_of_ingredients = randint(3, 6)
    print(number_of_ingredients, target_weight)

    # Generate n ingredients with random weights and values
    for _ in range(number_of_ingredients):
        weight = randint(1, 5)
        value = randint(1, 5)
        print(weight, value)
elif case_num == 1:
    target_weight = randint(10, 20)
    number_of_ingredients = randint(3, 6)
    print(number_of_ingredients, target_weight)

    # Generate n ingredients with random weights and values
    for _ in range(number_of_ingredients):
        weight = randint(1, 5)
        value = randint(1, 5)
        print(weight, value)
else:
    # output what should be read in as input by
    # contestant code
    target_weight = randint(10, 100000)
    number_of_ingredients = randint(5, 1000)
    print(number_of_ingredients, target_weight)

    # Generate n ingredients with random weights and values
    for _ in range(number_of_ingredients):
        weight = randint(1, 1000)
        value = randint(1, 100)
        print(weight, value)
