from collections import defaultdict
import sys

def debug(*args):
    if "debug" in sys.argv:
        print(*args, file=sys.stderr)


def run_case():
    n, total_company_members = map(int, input().split())
    assert n <= total_company_members
    all_names = input().split()
    higher_to_lower = defaultdict(set)
    lower_person_to_higher = defaultdict(set)
    min_approval_count_for_x = defaultdict(int)
    max_approval_count_for_x = defaultdict(int)
    all_members = set()
    remaining_requirement_count_for_x = defaultdict(int)
    for i in range(n):
        person_and_counts = input().split()
        higher_person = person_and_counts[0]
        cur_approvals_needed, total_lower_person_count = [int(x) for x in person_and_counts[1:]]

        higher_to_lower[higher_person] = {all_names[x] for x in list(map(int, (input().split())))}
        assert len(higher_to_lower[higher_person]) == total_lower_person_count
        remaining_requirement_count_for_x[higher_person] = cur_approvals_needed
        for required_person in higher_to_lower[higher_person]:
            lower_person_to_higher[required_person].add(higher_person)
        min_approval_count_for_x[higher_person] = cur_approvals_needed
        max_approval_count_for_x[higher_person] = total_lower_person_count
        all_members.add(higher_person)
        all_members |= higher_to_lower[higher_person]

    assert len(all_members) <= total_company_members
    #add members that were not listed
    debug("all_members", all_members)
    ret = total_company_members - len(all_members)

    debug(remaining_requirement_count_for_x)
    current_members_to_check = set()
    for person in all_members:
        if remaining_requirement_count_for_x[person] == 0:
            current_members_to_check.add(person)
            remaining_requirement_count_for_x.pop(person)
    ret += len(current_members_to_check)
    debug("ret", ret)
    #free up people with no requirements
    while True:
        debug("current members", current_members_to_check)
        next_time_members = set()
        for leaf_member in current_members_to_check:
            for higher_person in lower_person_to_higher[leaf_member]:
                if higher_person in remaining_requirement_count_for_x:
                    remaining_requirement_count_for_x[higher_person] -= 1
                    if remaining_requirement_count_for_x[higher_person] <= 0:
                        next_time_members.add(higher_person)
                        remaining_requirement_count_for_x.pop(higher_person)

        debug("next_time_members", next_time_members)
        if len(next_time_members) == 0:
            break
        ret += len(next_time_members)
        current_members_to_check = next_time_members.copy()
    
    return ret
    

cases = int(input())
for i in range(cases):
    print(run_case())