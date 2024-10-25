#!/usr/local/bin/python3
from random import randint, sample, choice, choices, seed
from string import ascii_lowercase
import sys
import re
case_num = int(input())
seed(case_num)
# 0 and 1 are the sample cases

def make_equation(symbols_to_use, min_length, use_paren=False):
    paren_depth = 0
    OPEN_PAREN = "("
    while True:
        result = choices(list(range(0, 21)), k=min_length)
        # print(result, file=sys.stderr)
        dummy_filler_symbol = "$"
        result = [str(x) for x in result]
        result = f" {dummy_filler_symbol} ".join(result).split()
        # print(result, file=sys.stderr)
        if use_paren:
            pos = 0
            while pos < len(result):
                if paren_depth > 0 and result[pos] == dummy_filler_symbol and randint(0, 3) == 0:
                    result.insert(pos , ")")
                    paren_depth -= 1
                if pos < len(result) // 2 and result[pos] == dummy_filler_symbol and randint(0, 1):
                    result.insert(pos + 1, "(")
                    paren_depth += 1
                pos += 1
            for i in range(paren_depth):
                result.append(")")
        
        joined_result = "".join(result)
        eq = joined_result.replace(dummy_filler_symbol, "+")
        try:
            confirm_valid = eval(eq)
        except:
            print("this was invalid", eq)
            exit(-1)
            continue
        for i in range(len(result)):
            if result[i] == dummy_filler_symbol:
                result[i] = choice(symbols_to_use)
        
        return " ".join(result)


if case_num == 0:
    print("wxyz")
    sample_symbols = '''
    w +
    x *
    y +
    z *
    '''
    for line in sample_symbols.strip().splitlines():
        print(line.strip())
    print(2)
    print("4 z 5 y 2 w 7")
    print("5 y 8 x 4 z 9 w 6")
# elif case_num == 1:
#     print("cats")
#     sample_symbols = '''
#     c +
#     a *
#     t -
#     s *
#     '''
#     for line in sample_symbols.strip().splitlines():
#         print(line.strip())
#     print(4)
#     print("4 t 5 a 2 c 7")
#     print("14 a -5 c 12 t 7")
#     print("2 s 7 t 6 t 100 c 5")
#     print("200 c 35 t 100 c 15")
# elif case_num == 2:
#     print("paren")
#     sample_symbols = '''
#     p +
#     a *
#     r -
#     e *
#     n *
#     '''
#     for line in sample_symbols.strip().splitlines():
#         print(line.strip())
#     print(3)
#     print("9 e ( 4 p 6 )")
#     print("2 p ( ( 5 e 4 ) r 6 a 8 ) e ( 10 e 5 )")
#     print("19 p 4 e ( 1 x 20 p ( 7 e 14 r ( 18 ) ) )")
else:
    # output what should be read in as input by
    # contestant code
    letter_count = randint(3, 6)
    order = "".join(sample(ascii_lowercase, letter_count))
    operators = ["*", "+", "-"]
    print(order)
    for letter in order:
        if case_num == 1 and letter == 'c':
            print(letter, '-')
        else:
            print(letter, choice(operators))
    equation_count = randint(3, 10)
    print(equation_count)
    for i in range(equation_count):
        if case_num == 1:
            print(make_equation(order, 4 + i // 2, True))
        elif case_num < 20:
            print(make_equation(order, 4))
        elif case_num < 30:
            print(make_equation(order, 7, True))
        else:
            print(make_equation(order, 20, True))
