from collections import defaultdict
from math import inf
n, target_weight = map(int, input().split())
weight_and_value = [tuple(map(int, input().split())) for i in range(n)]
weights = [line[0] for line in weight_and_value]
values = [line[1] for line in weight_and_value]
print(weight_and_value)

dp = defaultdict(int)
#cur_item_number is how many items were taken from the beginning of the list
for cur_item_number_x in range(n):
    for cur_cap_weight_y in range(0, target_weight + 1):
        # we can't take this item
        if cur_cap_weight_y-weights[cur_item_number_x] < 0:
            dp[cur_cap_weight_y, cur_item_number_x] = dp[cur_cap_weight_y, cur_item_number_x-1]
            continue
        else:
            dp[cur_cap_weight_y, cur_item_number_x] = max(
                    dp[cur_cap_weight_y, cur_item_number_x-1], 
                    dp[cur_cap_weight_y-weights[cur_item_number_x], cur_item_number_x-1] + values[cur_item_number_x]
            )        

for cur_cap_weight_y in range(1, target_weight + 1):
    print(cur_cap_weight_y, ":", end='\t')
    for cur_item_number_x in range(n):
        print(dp[cur_cap_weight_y, cur_item_number_x], end='\t')
    print()


print(dp[target_weight, n-1])