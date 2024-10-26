import math

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def find_solution(A, B, C):
    gcd, x, y = extended_gcd(A, B)
    
    # Check if C is divisible by gcd(A, B)
    if C % gcd != 0:
        return "No solution exists."
    
    # Scale the solution by C / gcd
    x *= C // gcd
    y *= C // gcd
    
    return f"Solution exists: a = {x}, b = {y}"

A = 2726
B = -7865
C = 2719

print(find_solution(A, B, C))
