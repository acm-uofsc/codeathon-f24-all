#!/usr/local/bin/python3
from random import randint, sample, choice, choices, seed, shuffle
from string import ascii_lowercase
import sys
import re
case_num = int(input())
seed(case_num * 555)
ascii_lowercase = list(ascii_lowercase)
shuffle(ascii_lowercase)
ascii_lowercase = "".join(ascii_lowercase)
def get_word(highest_ingredients_before, len_hi=100):
    return "".join(choices(ascii_lowercase[:highest_ingredients_before], k=randint(1, len_hi)))
# 0 and 1 are the sample cases
if case_num == 0:
    print(3)
    print("candyapples", "kitkat", "ssssswwwweeeeeeeeeeeeeeeeetttt")
elif case_num == 1:
    print(4)
    print("gum", "lollipop", "abcdef", "xyz")
else:
    n = randint(1, min(case_num ** 3, 100))
    highest_ingredients_before = randint(1, 25)
    word_size = randint(1, 100)
    candies = [get_word(highest_ingredients_before) for i in range(n-1)]

    highest_after = highest_ingredients_before + 1
    answer_entry = ascii_lowercase[:highest_after] + get_word(highest_after, randint(1, 70))
    answer_entry = list(answer_entry)
    shuffle(answer_entry)
    answer_entry = "".join(answer_entry)
    candies.append(answer_entry)
    print(n)
    print(" ".join(candies))
