import sys
sys.setrecursionlimit(10 ** 5 + 10)

number_of_vertex, number_of_edges = map(int, input().split())
start_node, goal_node = map(int, input().split())

start_node -= 1
goal_node -= 1

checked = [False] * number_of_vertex
edges = [[] for _ in range(number_of_vertex)]


for _ in range(number_of_edges):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)


def dfs(n):
    checked[n] = True
    for i in edges[n]:
        if not checked[i]:
            dfs(i)


dfs(start_node)

if checked[goal_node]:
    print("YES")
else:
    print("NO")


