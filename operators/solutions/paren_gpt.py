# Tokenizer helpers
def tokenize(expression):
    """ Converts the input expression string into a list of tokens """
    tokens = []
    i = 0
    while i < len(expression):
        if expression[i] in '()':
            tokens.append(expression[i])
            i += 1
        elif expression[i].isspace():
            i += 1
        else:
            j = i
            while j < len(expression) and expression[j].isalnum():
                j += 1
            tokens.append(expression[i:j])
            i = j
    return tokens

# Operator precedence map
precedence_map = {
    'W': 3,  # *
    'X': 2,  # +
    'Y': 1,  # +
    'Z': 0,  # *
}

# Parser helpers
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0

    def peek(self):
        """ Peek at the next token without consuming it """
        if self.current_token_index < len(self.tokens):
            return self.tokens[self.current_token_index]
        return None

    def advance(self):
        """ Move to the next token """
        if self.current_token_index < len(self.tokens):
            self.current_token_index += 1

    def parse_primary(self):
        """ Parse a primary expression (a number or an expression in parentheses) """
        token = self.peek()

        if token == '(':
            self.advance()  # consume '('
            expr_value = self.parse_expression()
            if self.peek() == ')':
                self.advance()  # consume ')'
            return expr_value
        else:
            self.advance()
            return int(token)

    def get_precedence(self, op):
        """ Get the precedence of the operator """
        return precedence_map.get(op, -1)

    def parse_expression(self):
        """ Parse the full expression starting with min precedence 0 """
        return self.parse_expression_1(self.parse_primary(), 0)

    def parse_expression_1(self, lhs, min_precedence):
        """ Recursively parse expressions based on precedence """
        lookahead = self.peek()

        while lookahead in precedence_map and self.get_precedence(lookahead) >= min_precedence:
            print(lookahead)
            op = lookahead
            self.advance()  # consume the operator

            rhs = self.parse_primary()  # parse the right-hand side
            lookahead = self.peek()

            # Handle right-associative operators or higher precedence
            while lookahead in precedence_map and (
                self.get_precedence(lookahead) > self.get_precedence(op) or
                (self.get_precedence(lookahead) == self.get_precedence(op))
            ):
                rhs = self.parse_expression_1(rhs, self.get_precedence(op) + 1)
                lookahead = self.peek()
                print("lookahead2", lookahead)

            # Apply the operation with lhs and rhs
            if op == 'W' or op == 'Z':  # Treat W and Z as multiplication
                lhs = lhs * rhs
            elif op == 'X' or op == 'Y':  # Treat X and Y as addition
                lhs = lhs + rhs

        return lhs

# Example usage
expression = "4 Z ( ( 2 Z 5 ) Z 6 Z 2 Y 9 )"  # This should evaluate as 4 * (5 + 2) = 28
tokens = tokenize(expression)
print(tokens)
parser = Parser(tokens)
result = parser.parse_expression()

print(f"The result of the expression '{expression}' is {result}")
