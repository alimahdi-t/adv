from collections import deque

n = int(input())  # Length of the permutation
start = list(map(int, input().split()))  # Initial permutation

goal = list(range(1, n + 1))  # Sorted target permutation (e.g., [1, 2, ..., n])

# Precompute factorials for 0 to n (used in encoding permutations)
factorial = [1] * (n + 1)
for i in range(2, n + 1):
    factorial[i] = factorial[i - 1] * i

# Convert a permutation into a unique integer code using Factoradic system
def perm_to_code(perm):
    code = 0
    used = [False] * (n + 1)
    for i in range(n):
        cnt = 0
        # Count how many smaller numbers haven't been used yet
        for j in range(1, perm[i]):
            if not used[j]:
                cnt += 1
        code += cnt * factorial[n - i - 1]
        used[perm[i]] = True
    return code

# Convert a Factoradic code back to the original permutation
def code_to_perm(code):
    numbers = list(range(1, n + 1))
    perm = []
    for i in range(n - 1, -1, -1):
        idx = code // factorial[i]
        code %= factorial[i]
        perm.append(numbers.pop(idx))  # Pick the idx-th unused number
    return perm

# BFS to find the minimum number of prefix reversals to sort the permutation
def bfs(start, goal):
    start_code = perm_to_code(start)
    goal_code = perm_to_code(goal)

    dist = [-1] * factorial[n]  # Distance array for all permutation codes
    dist[start_code] = 0  # Distance to start is 0

    queue = deque([start_code])  # Initialize BFS queue

    while queue:
        current_code = queue.popleft()

        # If we reached the goal, return distance
        if current_code == goal_code:
            return dist[current_code]

        current_perm = code_to_perm(current_code)  # Decode to get current permutation

        # Try all prefix reversals from position 1 to n
        for x in range(1, n + 1):
            next_perm = current_perm[:x][::-1] + current_perm[x:]  # Reverse first x elements
            next_code = perm_to_code(next_perm)

            if dist[next_code] == -1:  # If not visited yet
                dist[next_code] = dist[current_code] + 1
                queue.append(next_code)

    return -1  # Should not reach here; means goal is unreachable (which shouldn’t happen)

# Run and print the result
print(bfs(start, goal))  # Output the minimum number of prefix reversals to sort `start`
print(perm_to_code(start))  # Also print the code (ID) of the starting permutation
