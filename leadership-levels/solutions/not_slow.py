from collections import defaultdict, deque
import sys

def run_case():
    needs_approval_count, total_members = map(int, input().split())
    all_names  = input().split()
    person_to_remaining_approvals_needed = defaultdict(int)
    person_to_approver_names = defaultdict(list)
    higher_power_to_lower = defaultdict(list)
    person_to_min_count_needed = defaultdict(int)
    for i in range(needs_approval_count):
        person, min_needed, hi_allowed = input().split()
        min_needed = int(min_needed)
        person_to_min_count_needed[person] = min_needed
        hi_allowed = int(hi_allowed)
        person_to_remaining_approvals_needed[person] = min_needed
        approver_positions = [int(y) for y in input().split()]
        approver_names = [all_names[x] for x in approver_positions]
        person_to_approver_names[person] = approver_names
        for approver in approver_names:
            higher_power_to_lower[approver].append(person)

    changed = True
    given_approval = set()
    cur_names = all_names
    while changed:
        changed = False
        next_time = []
        for i in range(len(cur_names)):
            cur_name = cur_names[i]
            approvals_given = 0
            for approver in person_to_approver_names[cur_name]:
                if approver in given_approval:
                    approvals_given += 1
            if approvals_given >= person_to_min_count_needed[cur_name] and cur_name not in given_approval:
                given_approval.add(cur_name)
                changed = True
                next_time.extend(higher_power_to_lower[cur_name])
        cur_names = next_time.copy()
                
    return len(given_approval)


cases = int(input())
for i in range(cases):
    print(run_case())
