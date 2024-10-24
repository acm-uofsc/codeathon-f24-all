import sys
def solve():
    layer_count, slice_count = map(int, input().split())
    start_x, start_depth, goal_x, goal_depth = map(int, input().split())
    depth_change_cost, slice_change_cost = map(int, input().split())
    best = float("inf")
    #first try changing depth to exactly goal depth, then change position in ring
    slice_difference = abs(start_x - goal_x)
    for temp_goal_ring in range(1, layer_count + 1):
        #basically going in to the center, then back out to the goal location
        dist_from_start_to_temp = abs(temp_goal_ring - start_depth)
        dist_from_temp_to_goal = abs(temp_goal_ring - goal_depth)
        cur_cost = dist_from_start_to_temp * depth_change_cost + dist_from_temp_to_goal * depth_change_cost
        # print("dist_from_start_to_temp * depth_change_cost + dist_from_temp_to_goal * depth_change_cost\n", f"{dist_from_start_to_temp} * {depth_change_cost} + {dist_from_temp_to_goal} * {depth_change_cost}", "=", cur_cost, file=sys.stderr)

        # print("ring change cost:", cur_cost, file=sys.stderr)
        #"rotation" cost
        current_cost_to_change_slices = min(slice_difference, slice_count - slice_difference) * temp_goal_ring * slice_change_cost
        # print(f"slice_change_cost: {slice_change_cost}", file=sys.stderr)
        before = cur_cost
        cur_cost += current_cost_to_change_slices
        print(f"{before} + {current_cost_to_change_slices} = {cur_cost}", file=sys.stderr)
        # print("cur cost", cur_cost, file=sys.stderr)
        best = min(best, cur_cost)
    return best

cases = int(input())
for i in range(cases):
    print(solve())