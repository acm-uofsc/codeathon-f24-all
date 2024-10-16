#!/usr/local/bin/python3
from random import randint, sample, choice, choices, seed, shuffle
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

all_three_letter_names = [''.join(group) for group in it.product(ascii_lowercase, 
                                                            repeat=3)]
def number_to_letters(num):
    return all_three_letter_names[num % len(all_three_letter_names)]

def gen_single_case(case_num):
    if case_num < 10:
        total_people = randint(1, 30)
    elif case_num < 20:
        total_people = randint(600, 800)
    else:
        total_people = randint(97000 - 10, 97000)
    
    G = defaultdict(set)
    used = set()
    for i in range(1, 11):
        offset = randint(2, 10)*1000
        used.add(i)
        if len(used) == total_people:
            break
        for j in range(randint(0, 4)**2):
            cur = i*offset+j
            G[i].add(cur)
            used.add(cur)
            if len(used) == total_people:
                break
        if len(used) == total_people:
            break

    has_requirements = list(G.keys()) 
    has_requirements.sort()
    shuffle(has_requirements)
    print(len(has_requirements), total_people)
    for key in has_requirements:
        total_can_get_approval_from = len(G[key])
        print(
            number_to_letters(key), 
            randint(max(0, total_can_get_approval_from-3), total_can_get_approval_from),
            total_can_get_approval_from
        )
        connected_to = list(G[key])
        connected_to.sort()
        shuffle(connected_to)
        print(*[number_to_letters(x) for x in connected_to])
    

# 0 and 1 are the sample cases
if case_num == 0:
    print(2)
    print(3, 20)
    print("president", 3, 3)
    print("secretary HR vicePresident")
    print("secretary", 1, 3)
    print("HR janitor manager")
    print("vicePresident", 1, 1)
    print("secretary")
    print(4, 4)
    print("dead", 1, 1)
    print("lock")
    print("lock", 1, 1)
    print("key")
    print("key", 1, 1)
    print("shovel")
    print("shovel", 1, 1)
    print("dead")

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

    
