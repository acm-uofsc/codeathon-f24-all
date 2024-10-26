from collections import defaultdict, deque
import sys

def run_case():
    needs_approval_count, total_members = map(int, input().split())
    assert needs_approval_count <= total_members
    all_names  = input().split()
    assert len(set(all_names)) == len(all_names)
    person_to_remaining_approvals_needed = defaultdict(int)
    person_to_approver_names = defaultdict(list)
    higher_power_to_lower = defaultdict(list)
    person_to_min_count_needed = defaultdict(int)
    for i in range(needs_approval_count):
        person, min_needed, hi_allowed = input().split()
        min_needed = int(min_needed)
        person_to_min_count_needed[person] = min_needed
        hi_allowed = int(hi_allowed)
        assert min_needed <= hi_allowed, f"{min_needed}, {hi_allowed}"
        # assert len(can_approve_binary_string) == total_members
        person_to_remaining_approvals_needed[person] = min_needed
        approver_positions = [int(y) for y in input().split()]
        approver_names = [all_names[x] for x in approver_positions]
        person_to_approver_names[person] = approver_names
        assert person not in approver_names, person
        for approver in approver_names:
            higher_power_to_lower[approver].append(person)

    # print(fringe, file=sys.stderr)
    ret = 0
    changed = True
    given_approval = set()
    while changed:
        changed = False
        for i in range(len(all_names)):
            cur_name = all_names[i]
            approvals_given = 0
            for dependency in person_to_approver_names[cur_name]:
                if dependency in given_approval:
                    approvals_given += 1
            if approvals_given >= person_to_min_count_needed[cur_name] and cur_name not in given_approval:
                given_approval.add(cur_name)
                changed = True
                
    assert ret <= total_members
    # for x in given_approval:
    #     print(x, "approved", file=sys.stderr)
    return len(given_approval)


cases = int(input())
for i in range(cases):
    print(run_case())
