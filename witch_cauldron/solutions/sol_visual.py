from collections import defaultdict

def make_dp(n, weight_and_value, highest_cap=1500):
    weights = [line[0] for line in weight_and_value]
    values = [line[1] for line in weight_and_value]
    dp = defaultdict(int)
    #cur_item_number is how many items were taken from the beginning of the list
    for cur_item_number_x in range(n):
        for cur_cap_weight_y in range(0, highest_cap + 1):
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

case_count = int(input())
to_answer = []
highest_cap = 0
for i in range(case_count):
    max_cap, first_x_items = map(int, input().split())
    to_answer.append((max_cap, first_x_items))
    highest_cap = max(highest_cap, max_cap)
    
dp = make_dp(n, weight_and_value, highest_cap)

for max_cap, first_x_items in to_answer:
    print(dp[max_cap, first_x_items-1])
    
for cur_cap_weight_y in range(0, highest_cap + 1):
    for cur_item_number_x in range(n):
        print(dp[cur_cap_weight_y, cur_item_number_x], end=',')
    print()
