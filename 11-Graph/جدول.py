n = int(input())

m = [list(map(int, input().split())) for _ in range(n)]

print(m)
edges = [[] for _ in range(n)]

for i in range(n - 1):
    for j in range(n):
        if i == j:
            continue
        if i == 0 and j != n - 1:
            print("hey")
            if m[i][j] == m[i][j + 1]:
                edges[i][j].append(j)
                edges[j].append(i)

            pass
        elif i == n - 1:
            pass
        if j == 0:
            pass
        elif j == n - 1:
            pass
print(edges)