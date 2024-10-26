#!/usr/local/bin/python3
from random import randint, sample, choice, choices, seed, shuffle, uniform
from string import ascii_lowercase, ascii_letters
from collections import deque
import itertools as it
import sys
import re
from collections import defaultdict
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

def gen_basically_all_used_case(total_base=80000, depend_count=10):
    total_people = (total_base - randint(0, 100))
    if total_people <= 100:
        total_people = total_base
    names_to_use = sample(all_four_letter_names, k=total_people)
    people_to_depend_on_numbers = list(range(total_people))
    shuffle(people_to_depend_on_numbers)
    fringe = people_to_depend_on_numbers
    seen = set()
    seen_list = []
    dependency_numbers_for_number = defaultdict(set)
    while fringe:
        if len(fringe) < 20 and randint(0,3) == 0:
            break
        if len(fringe) == 2:
            break
        cur = fringe.pop()
        # for i in range(min(3, len(seen))):
        if len(seen) > 0:
            dependency_numbers_for_number[cur] |= set(sample(seen_list, k=min(depend_count, len(seen))))
        seen.add(cur)
        seen_list.append(cur)
        if len(seen_list) > depend_count + 10:
            seen_list.pop(0)
        
    for i in range(len(fringe)):
        dependency_numbers_for_number[fringe[i]].add(fringe[i-1])

    print(len(dependency_numbers_for_number), total_people)
    print(*names_to_use)
    for key in dependency_numbers_for_number:
        print(names_to_use[key], randint(1, len(dependency_numbers_for_number[key])), len(dependency_numbers_for_number[key]))
        print(*dependency_numbers_for_number[key])

    

def gen_simple_case(case_num):
    # gen_basically_all_used_case(1_000, 3)
    GOAL_PRODUCT = 4000
    total_people = case_num * 50
    if case_num < 3:
        total_people = case_num + 8
        GOAL_PRODUCT = 30
    # if case_num <= 4:
    #     total_people = case_num + 8
    # elif case_num < 10:
    #     total_people = randint(20, 25)
    # elif case_num < 20:
    #     total_people = randint(1000, 2000)
    #     GOAL_PRODUCT = 30_000
    # elif case_num < 35:
    #     GOAL_PRODUCT = 300_000
    #     hi = 80000
    #     total_people = randint(hi - 10, hi)
    # else:
    #     GOAL_PRODUCT = 6_000_000
    #     hi = 80000
    #     total_people = randint(hi - 10, hi)
    
    names_to_use = sample(all_four_letter_names, k=total_people)
    person_to_dependencies = {}
    people_to_depend_on = list(range(total_people))
    for i in range(int(total_people * uniform(.8, 1))):
        cur_person_with_dependencies = names_to_use[i]

        depend_count = randint(0, 8)
        if case_num >= 15 and randint(0, 4):
            depend_count = randint(10, max(10, GOAL_PRODUCT // total_people))
            depend_count = randint(8, 10)
        depend_count = min(depend_count, total_people -3)
        starting_pos = (i*(12 + 1 + randint(20, 2000))) % len(people_to_depend_on)

        people_to_depend_on_slice = people_to_depend_on[starting_pos:starting_pos+depend_count]
        if i in people_to_depend_on_slice:
            people_to_depend_on_slice.remove(i)
        if len(people_to_depend_on_slice) == 0:
            people_to_depend_on_slice = [people_to_depend_on[i-1]]

        person_to_dependencies[cur_person_with_dependencies] = people_to_depend_on_slice
    
    print(len(person_to_dependencies), total_people)
    print(*names_to_use)
    for higher_up in person_to_dependencies:
        dependency_count = len(person_to_dependencies[higher_up])
        amount_needed = int(dependency_count * uniform(.3, 1.1))
        amount_needed = min(amount_needed, dependency_count)
        amount_needed = max(amount_needed, 0)
        if case_num > 30:
            amount_needed = dependency_count // 2
        print(higher_up, amount_needed, dependency_count)
        shuffle(person_to_dependencies[higher_up])
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
elif case_num == 1:
    case_count = 3
    print(case_count)
    gen_basically_all_used_case(14, 8)
    for i in range(case_count-1):
        gen_simple_case(i)

else:
    case_count = randint(5, 15)
    print(case_count)
    for t in range(case_count):
        if case_num in range(0, 10):
            gen_simple_case(case_num)
        elif case_num in range(10, 20):
            gen_basically_all_used_case(1_000, 7)
        elif case_num in range(20, 30):
            gen_basically_all_used_case(4_000, 3)
        elif case_num in range(30, 50):
            if t == 0:
                gen_basically_all_used_case(80_000, 2)
            elif t == 1:
                gen_basically_all_used_case(500, 7)
            else:
                gen_simple_case(7)

    
