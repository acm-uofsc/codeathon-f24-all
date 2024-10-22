from collections import defaultdict
from math import inf
import sys
def make_dp(n, weight_and_value, highest_target=1501):
    weights = [line[0] for line in weight_and_value]
    values = [line[1] for line in weight_and_value]

    dp = defaultdict(int)
    #cur_item_number is how many items were taken from the beginning of the list
    for cur_item_number_x in range(n):
        for cur_cap_weight_y in range(0, highest_target + 1):
            # we can't take this item
            if cur_cap_weight_y-weights[cur_item_number_x] < 0:
                dp[cur_cap_weight_y, cur_item_number_x] = dp[cur_cap_weight_y, cur_item_number_x-1]
            else:
                dp[cur_cap_weight_y, cur_item_number_x] = max(
                        dp[cur_cap_weight_y, cur_item_number_x-1], 
                        dp[cur_cap_weight_y-weights[cur_item_number_x], cur_item_number_x-1] + values[cur_item_number_x]
                )
    return dp

n = int(input())
weight_and_value = [tuple(map(int, input().split())) for i in range(n)]
dp = make_dp(n, weight_and_value)
# for cur_cap_weight_y in range(1, 25 + 1):
#     print(cur_cap_weight_y, ":", end='\t', file=sys.stderr)
#     for cur_item_number_x in range(n):
#         print(dp[cur_cap_weight_y, cur_item_number_x], end='\t', file=sys.stderr)
#     print(file=sys.stderr)
case_count = int(input())
for i in range(case_count):
    max_cap, first_x_items = map(int, input().split())
    # print("max_cap, first_x_items", file=sys.stderr)
    # print(max_cap, first_x_items, file=sys.stderr)
    # max_cap = min(max_cap, )
    print(dp[max_cap, first_x_items-1])
    

