#!/usr/local/bin/python3
from random import randint, sample, choice, choices, seed, shuffle, uniform
from string import ascii_lowercase, ascii_letters
import itertools as it
import sys
import re
from collections import defaultdict
import graphlib
case_num = int(input())
seed(case_num * 234)
ascii_lowercase = list(ascii_lowercase)
shuffle(ascii_lowercase)
ascii_lowercase = "".join(ascii_lowercase)

def get_name():
    return ''.join(choices(ascii_lowercase, k=3))

all_four_letter_names = [''.join(group) for group in it.product(ascii_lowercase, 
                                                            repeat=4)]
def number_to_letters(num):
    return all_four_letter_names[num % len(all_four_letter_names)]

def gen_single_case(case_num):
    if case_num < 10:
        total_people = randint(20, 25)
    elif case_num < 20:
        total_people = randint(600, 800)
    else:
        hi = 80000
        total_people = randint(hi - 10, hi)
    
    names_to_use = sample(all_four_letter_names, k=total_people)
    person_to_dependencies = {}
    people_to_depend_on = list(range(total_people))
    for i in range(int(total_people * uniform(.8, 1))):

        # print(i, file=sys.stderr)
        cur_person_with_dependencies = names_to_use[i]
        # if i > 0:
        #     people_to_depend_on.add(i-1)
        # people_to_depend_on.remove(i)
        # if i % 300 == 0:
        #     shuffle(people_to_depend_on)
        depend_count = randint(2, 7)
        # depend_count = min(depend_count, len(people_to_depend_on))
        starting_pos = (i*12 + 1 + randint(20, 200)) % len(people_to_depend_on)
        # if starting_pos + depend_count >= len(people_to_depend_on):
            # starting_pos = 0
        depend_count = max(depend_count, 1)
        people_to_depend_on_slice = people_to_depend_on[starting_pos:starting_pos+depend_count]
        if i in people_to_depend_on_slice:
            people_to_depend_on_slice.remove(i)
        if len(people_to_depend_on_slice) == 0:
            people_to_depend_on_slice = people_to_depend_on[i-1]
        # mask = [0]*total_people
        # for other_person_num in people_to_depend_on:
        #     mask[other_person_num] = 1
        person_to_dependencies[cur_person_with_dependencies] = people_to_depend_on_slice
    
    print(len(person_to_dependencies), total_people)
    print(*names_to_use)
    for higher_up in person_to_dependencies:
        dependency_count = len(person_to_dependencies[higher_up])
        amount_percent_needed = int(dependency_count * uniform(.3, 1.1))
        amount_percent_needed = min(amount_percent_needed, dependency_count)
        print(higher_up, amount_percent_needed, dependency_count)
        print(*person_to_dependencies[higher_up])

    

# 0 and 1 are the sample cases
if case_num == 0:
    print(2)
    print(3, 8)
    print("president secretary HR vicePresident janitor manager grace nia")
    print("president", 3, 3)
    print(1, 2, 3)
    print("secretary", 1, 3)
    print(2, 4, 5)
    print("vicePresident", 1, 1)
    print(0)
    print(4, 5)
    print("dead lock key shovel axe")
    print("dead", 1,   1)
    print(1)
    print("lock", 1,   1)
    print(2)
    print("key", 1,    1)
    print(3)
    print("shovel", 1, 1)
    print(0)

else:
    case_count = randint(5, 15)
    print(case_count)
    if case_num < 20:
        for t in range(case_count):
            gen_single_case(case_num)
    else:
        gen_single_case(case_num)
        for t in range(case_count-1):
            gen_single_case(7)

    
