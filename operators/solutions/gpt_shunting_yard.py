import operator as op
# Define precedence and associativity
# precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
'''
1. Create an empty output queue and an empty operator stack.
2. For each token in the expression:
    a. If the token is a number (operand), add it to the output queue.
    b. If the token is an operator (like +, -, *, /):
        i. While there is an operator on the top of the stack with greater precedence (or equal precedence if left associative):
            - Pop the operator from the stack to the output queue.
        ii. Push the current operator onto the stack.
    c. If the token is a left parenthesis '(', push it onto the stack.
    d. If the token is a right parenthesis ')':
        i. While the operator at the top of the stack is not a left parenthesis '(':
            - Pop the operator from the stack to the output queue.
        ii. Pop the left parenthesis '(' from the stack and discard it.
3. After the loop, pop all the operators from the stack to the output queue.
'''

def is_operator(token):
    return token in precedence

def shunting_yard(expression):
    output_queue = []
    operator_stack = []
    
    tokens = expression.split()  # Split the expression by spaces for simplicity
    # print("tokens", tokens)
    for token in tokens:
        if token[-1].isdigit():  # If the token is an operand (number)
            output_queue.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            operator_stack.pop()  # Remove the '(' from stack
        elif is_operator(token):
            while (operator_stack and operator_stack[-1] != '(' and
                   (precedence[operator_stack[-1]] > precedence[token] or
                   precedence[operator_stack[-1]] == precedence[token])):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
    
    # Pop all the remaining operators in the stack to the output queue
    while operator_stack:
        output_queue.append(operator_stack.pop())
    
    return output_queue

def evaluate_postfix(postfix):
    stack = []
    # print("postfix", postfix)
    for token in postfix:
        if token[-1].isdigit():
            stack.append(int(token))
        elif is_operator(token):
            b = stack.pop()
            a = stack.pop()
            stack.append(letter_to_operator[token](a, b))
    
    return stack[0]  # The result is the only value left in the stack

# Example usage
expression = "3 + 4 * ( 6 - 2 )"  # Infix expression (note spaces between tokens)
expression = "5 y 8 x 4 z 9 w 6"
paren_string = "2 z ( ( 5 z 4 ) y 6 x 8 ) w ( 10 z 5 )"
paren_string = "( 2 y 5 w ( 4 x 3 ) w 10 ) w 1000"
paren_string = "5 y 8 x 4 z 9 w 6"
paren_string = "2 z ( ( 5 z 4 ) y 6 x 8 ) w ( 10 z 5 )" #should be 236
paren_string = "2 w ( ( 5 z 4 ) y 6 x 8 ) z ( 10 z 5 )" #should be 3500
expression = paren_string

'''
5 y 32 z 15
'''
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

precedence = {letter : len(order) - i for i, letter in enumerate(order)}

case_count = int(input())
for i in range(case_count):
    equation = input()
    postfix = shunting_yard(equation)
    result = evaluate_postfix(postfix)
    print(result)
