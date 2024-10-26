from collections import defaultdict

def parse_approval_structure():
    cases = int(input().strip())
    results = []

    for _ in range(cases):
        needs_approval_count, total_members = map(int, input().split())
        all_names = input().split()
        
        # Map to store approval requirements
        higher_power_to_lower = defaultdict(list)
        person_to_min_needed = defaultdict(int)
        # Process each member with dependencies
        for _ in range(needs_approval_count):
            person, min_needed, hi_allowed = input().split()
            min_needed = int(min_needed)
            hi_allowed = int(hi_allowed)
            person_to_min_needed[person] = min_needed

            # Get positions of approvers
            approver_positions = list(map(int, input().split()))
            approver_names = [all_names[pos] for pos in approver_positions]

            # For each approver, add the dependency relationship
            for approver in approver_names:
                higher_power_to_lower[approver].append(person)

        # Generate output in x -> y format
        case_output = []
        for approver, dependents in higher_power_to_lower.items():
            for dependent in dependents:
                case_output.append(f"{approver} ({person_to_min_needed[approver]}) -> {dependent} ({person_to_min_needed[dependent]})")
        
        results.append("\n".join(case_output))
    
    # Print results for each case
    for i, result in enumerate(results):
        print(f"Case {i+1} Output:\n{result}\n")

# Run the function to parse input and output relationships
parse_approval_structure()
