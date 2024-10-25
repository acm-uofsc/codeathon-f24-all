from collections import deque, defaultdict

def topological_sort(n, m, approvals):
    graph = defaultdict(list)
    indegree = defaultdict(int)
    all_people = set()
    
    # Building the graph
    for person, req_approvals, approvers in approvals:
        for i in range(len(approvers)):
            if approvers[i] == '1':
                graph[approvals[i][0]].append(person)  # person depends on approvers[i]
                indegree[person] += 1
        all_people.add(person)
    
    # Find all people who don't require anyone else's approval
    queue = deque([person for person in all_people if indegree[person] == 0])
    
    # Topological sort
    approved_count = 0
    while queue:
        current = queue.popleft()
        approved_count += 1
        
        for neighbor in graph[current]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    # The remaining members who don't require approval
    total_approved = (m - len(approvals)) + approved_count
    return total_approved

def main():
    t = int(input().strip())  # Number of test cases
    for _ in range(t):
        n, m = map(int, input().strip().split())  # n: number of approvals required, m: total members
        approvals = []
        people = input().split()
        for i in range(n):
            person, req_approvals, approvers = input().split()
            req_approvals = int(req_approvals)
            approvals.append((person, req_approvals, approvers))
        
        # Solve for each test case using topological sort
        result = topological_sort(n, m, approvals)
        print(result)

if __name__ == "__main__":
    main()
