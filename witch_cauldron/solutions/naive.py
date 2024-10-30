from collections import defaultdict
from itertools import combinations

n = int(input())
weight_and_value = [tuple(map(int, input().split())) for i in range(n)]
weights = [w for w, v in weight_and_value]
values = [v for w, v in weight_and_value]

case_count = int(input())
for i in range(case_count):
    max_cap, first_x_items = map(int, input().split())
    best = 0
    for combo_size in range(1, first_x_items + 1):
        for combo in combinations(weight_and_value[:first_x_items], combo_size):
            weight_total = sum(w for w, v in combo)
            if weight_total <= max_cap:
                value_total = sum(v for w, v in combo)
                before = best
                best = max(best, value_total)
    print(best)

