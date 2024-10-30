from collections import deque, defaultdict

def solve():
    a, b, x = map(int, input().split())
    bounds = 30000

    fringe = deque([(0, 1)])
    seen = defaultdict(lambda : -1)
    while fringe:
        cur, steps = fringe.popleft()
        if abs(cur) > bounds or cur in seen:
            continue
        seen[cur] = steps
        if cur == x:
            break
        fringe.append((cur + a, steps + 1))
        fringe.append((cur - b, steps + 1))
    print(seen[x])

cases = int(input())
for i in range(cases):
    solve()