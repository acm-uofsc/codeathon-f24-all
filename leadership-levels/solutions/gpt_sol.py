from collections import defaultdict, deque

def solve_approval_chain():
    t = int(input())  # number of test cases
    for _ in range(t):
        n, a = map(int, input().split())  # n: number of dependencies, a: total number of people at the company
        
        # Graph representation
        graph = defaultdict(list)  # people requiring approvals (x depends on y)
        indegree = defaultdict(int)  # count of approvals required for each person
        all_people = set()  # to keep track of all people mentioned
        
        for _ in range(n):
            # Reading each person's requirement
            x, u, d = input().split()  # person x requires u approvals from d others
            u, d = int(u), int(d)
            approvers = input().split()  # list of people x needs approval from
            
            all_people.add(x)
            indegree[x] = u  # initial indegree count for person x
            for approver in approvers:
                graph[approver].append(x)  # approver influences x
                all_people.add(approver)
        
        # Start BFS/DFS from people with 0 indegree (those who can approve without dependencies)
        queue = deque()
        for person in all_people:
            if indegree[person] == 0:
                queue.append(person)
        
        approved_count = 0
        approved = set()  # keep track of people who have approved
        
        while queue:
            current = queue.popleft()
            if current in approved:
                continue
            approved.add(current)
            approved_count += 1
            
            # Process people who depend on this current person
            for dependent in graph[current]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    queue.append(dependent)
        
        # Add people who never appeared in the dependency graph (no dependencies)
        approved_count += a - len(all_people)
        
        print(approved_count)

# Example usage:
solve_approval_chain()
