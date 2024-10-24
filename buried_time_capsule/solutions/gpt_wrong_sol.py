import sys
from collections import deque

def min_moves(a, b, x):
    # Edge case: if x is 0, no moves are needed
    if x == 0:
        return 0
    
    # Initialize BFS
    queue = deque([(0, 0)])  # Start at step 0 with 0 moves
    visited = set([0])       # Keep track of visited steps
    
    # Perform BFS
    while queue:
        current_step, moves = queue.popleft()
        
        # Move up by 'a' steps
        up_step = current_step + a
        if up_step == x:
            return moves + 2  # Found the target step
        if up_step <= x and up_step not in visited:  # Only consider valid unvisited steps
            visited.add(up_step)
            queue.append((up_step, moves + 1))
        
        # Move down by 'b' steps
        down_step = current_step - b
        if down_step == x:
            return moves + 2  # Found the target step
        if down_step >= 0 and down_step not in visited:  # Only consider valid unvisited steps
            visited.add(down_step)
            queue.append((down_step, moves + 1))
    
    # If BFS completes without finding the target, return -1 (unreachable)
    return -1

# Read input from stdin
input_data = input()  

# Parse the input (a, b, x)
a, b, x = map(int, input_data.split())

# Compute the minimum number of moves
result = min_moves(a, b, x)
    
# Output the result
print(result)