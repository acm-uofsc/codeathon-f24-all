from collections import defaultdict, deque
import sys
total_d_i = 0
total_a = 0
def run_case():
    global total_a, total_d_i
    needs_approval_count, total_members = map(int, input().split())
    total_a += total_members
    assert needs_approval_count <= total_members
    all_names  = input().split()
    assert len(set(all_names)) == len(all_names)
    name_to_index = {all_names[i] : i for i in range(len(all_names))}
    person_to_remaining_approvals_needed = defaultdict(int)
    person_to_approver_names = defaultdict(list)
    higher_power_to_lower = defaultdict(list)
    for i in range(needs_approval_count):
        person, min_needed, hi_allowed = input().split()
        min_needed = int(min_needed)
        hi_allowed = int(hi_allowed)
        total_d_i += hi_allowed
        assert min_needed <= hi_allowed, f"{min_needed}, {hi_allowed}"
        # assert len(can_approve_binary_string) == total_members
        person_to_remaining_approvals_needed[person] = min_needed
        approver_positions = [int(y) for y in input().split()]
        assert name_to_index[person] not in approver_positions
        approver_names = [all_names[x] for x in approver_positions]
        assert person not in approver_names
        person_to_approver_names[person] = approver_names
        assert person not in approver_names, person
        for approver in approver_names:
            higher_power_to_lower[approver].append(person)

    fringe = deque([name for name in all_names if person_to_remaining_approvals_needed[name] == 0])
    # print(fringe, file=sys.stderr)
    seen = {}
    ret = 0
    while fringe:
        cur_name = fringe.pop()
        if cur_name in seen:
            continue
        seen[cur_name] = True
        if person_to_remaining_approvals_needed[cur_name] <= 0:
            ret += 1
            for lower_down_person in higher_power_to_lower[cur_name]:
                person_to_remaining_approvals_needed[lower_down_person] -= 1
                if person_to_remaining_approvals_needed[lower_down_person] <= 0:
                    fringe.append(lower_down_person)
    assert ret <= total_members
    return ret


cases = int(input())
for i in range(cases):
    print(run_case())

print(f"{total_d_i} {total_a} {total_d_i + total_a}", file=sys.stderr)