import operator as op
import re
import sys
'''
similar to PEMDAS, (parenthesis, exponent, etc), we define letters of the alphabet, like WXYZ, and define the operation of each symbol
W is +
X is *
Y is +
Z is *
but the order of precedence is WXYZ
so 4 z 5 y 2
is equivalent to 
4 * (5 + 2) since y has higher precedence than Z
which is equal to 4 * 7 = 28
'''
order = "wxyz"
expression = "4 z 5 y 2 w 7 x 2 w 5"
letter_to_operator = {
    "w" : op.add,
    "x" : op.mul,
    "y" : op.add,
    "z" : op.mul,
}
operator_to_precedence = {letter : len(order) - i for i, letter in enumerate(order)}

def process_string_input(expression_string):
    return [int(x) if x.isnumeric() else x for x in expression_string.split()]

def solve_expression_without_paren(parts):
    # parts = process_string_input()
    assert "(" not in parts
    print('got this', parts)
    for letter in order:
        i = 1
        while i < len(parts) - 1:
            if parts[i] == letter:
                parts[i-1:i+2] = [letter_to_operator[letter](parts[i-1], parts[i+1])]
            else:
                i += 1
            print(parts)
    return parts[0]

def parse_until_paren_depth_0(expression):
    '''assumes that first element in expression is '(' 
    returns that first expression, and what comes after as a
    tuple'''
    depth = int(expression[0] == "(")
    pos = 1
    while pos < len(expression) and depth > 0:
        match expression[pos]:
            case "(":
                depth += 1
            case ")":
                depth -= 1
        pos += 1
    return expression[1:pos-1], expression[pos:]  

def parse_until_precedence_threshold_hit(expression, precedence_threshold):
    '''assumes that first element in expression is '(' 
    returns that first expression, and what comes after as a
    tuple'''
    pos = 0
    while pos < len(expression):
        match expression[pos]:
            case "(":
                depth += 1
            case ")":
                depth -= 1
        pos += 1
    return expression[1:pos-1], expression[pos:]  

# def parse_until_precedence_threshold_hit(expression, precedence_threshold=-1):



def solve_expression_paren_allowed(expression, precedence_threshold=-1):
    # left_side = None
    # most_recent_operator = lambda _, y : y
    i = 0
    left_side_stack = []
    print(expression)
    while i < len(expression):
        match expression[i]:
            case int():
                left_side_stack.append(expression[i])
                i += 1
                continue
            case "(":
                expression_in_paren, rest = parse_until_paren_depth_0(expression[i:])
                paren_part_solution = solve_expression_paren_allowed(expression_in_paren)
                return solve_expression_paren_allowed(left_side_stack + [paren_part_solution] + rest)
            case ")":
                i += 1
                continue
            case str(): #operator
                current_op_precedence = operator_to_precedence[expression[i]]
                if current_op_precedence < precedence_threshold:
                    return left_side_stack + expression[i:]
                # precedence_threshold = current_op_precedence
                if i + 2 < len(expression):
                    operator_two_spaces_later = expression[i+2]
                    if operator_two_spaces_later not in operator_to_precedence:
                        # a parenthesis messed up the parody, fall through to that case
                        left_side_stack.append(expression[i])
                        i += 1
                        continue
                    if operator_to_precedence[operator_two_spaces_later] <= precedence_threshold:
                        #solve the current expression, the one following will not interfere
                        current_spot_solution = letter_to_operator[expression[i]](left_side_stack[0], expression[i+1])
                        return [current_spot_solution] + expression[i+2:] 
                    else:
                        # the next operator was a higher precedence, solve what comes after this,
                        # then come back
                        left_side_stack.append(expression[i])
                        return solve_expression_paren_allowed(solve_expression_paren_allowed(expression[i+1:]))
                else:
                    return letter_to_operator[expression[i]](left_side, expression[i + 1])
    return left_side or 0

def process_string_and_solve(x):
    return solve_expression_without_paren(process_string_input(x))

def regex_match_eater(match: re.Match):
    print("eater got", match.group())
    return match.group(1) + str(process_string_and_solve(match.group(2)[1:-1])) + match.group(3)

def regex_cheese(starting_expression):
    before = starting_expression
    # print()
    # print("find result", re.findall(r".*(\(.+?\))", before))
    while (result := re.sub(r"(.*)(\(.+?\))(.*)", regex_match_eater, before)) != before:
        before = result
        print("after", result)
    return process_string_and_solve(result)



paren_string = "5 z 4 w 6"
paren_string = "5 x 4 w 6"
paren_string = "5 x 4 y 6"
paren_string = "9 z ( 4 w 6 )"
paren_string = "2 w ( ( 5 z 4 ) y 6 x 8 ) z ( 10 z 5 )"
paren_string = "5 y 8 x 4 z 9 w 6" # 555
paren_string = "2 z ( ( 5 z 4 ) y 6 x 8 ) w ( 10 z 5 )" #236
paren_string = "5 z ( 4 w 6 )" # 50
paren_string = "5 z 8 z 4 w 6"
paren_string = "( 2 y 5 w ( 4 x 3 ) w 10 ) w 1000"

# def wikipedia_parse_solution(lhs, min_precedence):
#     lookahead = peek next token
#     while lookahead is a binary operator whose precedence is >= min_precedence
#         op = lookahead
#         advance to next token
#         rhs = parse_primary ()
#         lookahead = peek next token
#         while lookahead is a binary operator whose precedence is greater
#                  than op's, or a right-associative operator
#                  whose precedence is equal to op's
#             rhs = parse_expression_1 (rhs, precedence of op + (1 if lookahead precedence is greater, else 0))
#             lookahead = peek next token
#         lhs = the result of applying op with operands lhs and rhs
#     return lhs

'''
( 2 y 5 w ( 4 x 3 ) w 10 ) w 1000
( 2 y 5 w 12 w 10 ) w 1000
( 2 y 17 w 10 ) w 1000
( 2 y 27 ) w 1000
29 w 1000
1029
'''

# def paren_cheese(starting_string: str):
#     for i, operator in enumerate(order):
#         starting_string = starting_string.replace(operator, )

# print(solve_expression_paren_allowed(process_string_input(paren_string)))
print(regex_cheese(paren_string))
