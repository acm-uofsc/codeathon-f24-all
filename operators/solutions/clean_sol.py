import operator as op
import re


def process_string_input(expression_string):
    return [int(x) if x[-1].isnumeric() else x for x in expression_string.split()]

def solve_expression_without_paren(parts):
    assert "(" not in parts
    for letter in order:
        i = 1
        while i < len(parts) - 1:
            # print(i, parts)
            if parts[i] == letter:
                parts[i-1:i+2] = [letter_to_operator[letter](parts[i-1], parts[i+1])]
            else:
                i += 1
            # print(parts)
    return parts[0]

def process_string_and_solve(x):
    return solve_expression_without_paren(process_string_input(x))

def regex_match_eater(match: re.Match):
    # print("eater got", match.group())
    return match.group(1) + str(process_string_and_solve(match.group(2)[1:-1])) + match.group(3)

def regex_cheese(starting_expression):
    before = starting_expression
    while (result := re.sub(r"(.*)(\(.+?\))(.*)", regex_match_eater, before)) != before:
        before = result
        # print("after", result)
    return process_string_and_solve(result)


order = input()
symbol_to_function = {
    "+" : op.add,
    "-" : op.sub,
    "*" : op.mul,
}

letter_to_operator = {}
for i in range(len(order)):
    letter, operator_symbol = input().split()
    letter_to_operator[letter] = symbol_to_function[operator_symbol]

operator_to_precedence = {letter : len(order) - i for i, letter in enumerate(order)}

case_count = int(input())
for i in range(case_count):
    equation = input()
    print(regex_cheese(equation))
