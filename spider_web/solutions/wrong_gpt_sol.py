def min_energy(L, S, d, r, x, y, a, b):
    # Calculate layer movement cost
    layer_cost = abs(y - b) * d
    
    # Calculate section movement cost (considering wraparound)
    section_diff = abs(x - a)
    section_cost = min(section_diff, S - section_diff) * r * L
    
    # Total cost
    total_cost = layer_cost + section_cost
    return total_cost

# Main function to process multiple test cases
def main():
    t = int(input())  # Number of test cases
    results = []
    
    for _ in range(t):
        # Read each test case
        L, S = map(int, input().split())  # Number of layers and sections
        x, y, a, b = map(int, input().split())  # Sunny's position and fly's position
        d, r = map(int, input().split())  # Costs
        
        # Compute the minimum energy for the current test case
        result = min_energy(L, S, d, r, x, y, a, b)
        results.append(result)
    
    # Output results for all test cases
    for res in results:
        print(res)

# Run the main function to read input and process cases
if __name__ == "__main__":
    main()
