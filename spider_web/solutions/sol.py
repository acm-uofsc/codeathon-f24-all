def solve():
    layer_count, section_count = map(int, input().split())
    start_x, start_depth, goal_x, goal_depth = map(int, input().split())
    depth_change_cost, section_change_cost = map(int, input().split())
    best = float("inf")
    #first try changing depth to exactly goal depth, then change position in ring
    section_difference = abs(start_x - goal_x)
    for temp_goal_depth in range(1, layer_count + 1):
        dist_from_start_to_temp = abs(temp_goal_depth - start_depth)
        dist_from_temp_to_goal = abs(temp_goal_depth - goal_depth)
        cur_cost = dist_from_start_to_temp * depth_change_cost + dist_from_temp_to_goal * depth_change_cost
        #"rotation" cost
        cur_cost += min(section_difference, section_count - section_difference) * temp_goal_depth * section_change_cost
        best = min(best, cur_cost)
    return best

cases = int(input())
for i in range(cases):
    print(solve())