import sys
sys.setrecursionlimit(10**7)

# n: number of vertexes
# m: number of edges
n, m = map(int, input().split())
edges = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
depth = [-1] * (n + 1)

# add edges
for _ in range(m):
    u, v = map(int, input().split())
    edges[v].append(u)
    edges[u].append(v)


def dfs(u, d):
    visited[u] = True
    depth[u] = d
    for neighbor in edges[u]:
        if not visited[neighbor]:
            dfs(neighbor, d+1)


for i in range(1, n + 1):
    if not visited[i]:
        if len(edges[i]) == 0:
            print("No")
            sys.exit()
        dfs(i, 0)

color = ["0"] * n

for i in range(1, n + 1):
    if depth[i] % 2 == 0:
        color[i - 1] = "1"
    else:
        color[i - 1] = "0"


print("Yes")
print("".join(color))

