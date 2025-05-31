n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(m)] for _ in range(n)]


dp[n - 1][0] = arr[n - 1][0]

for i in range(1, m):
    dp[n - 1][i] = dp[n - 1][i - 1] + arr[n - 1][i]

for i in range(n - 2, -1, -1):
    dp[i][0] = dp[i + 1][0] + arr[i][0]

path = ""
for i in range(n - 2, -1, -1):
    for j in range(1, m):
        dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]) + arr[i][j]


print(dp[0][m - 1])
# backtrack to build the path
path = ""
i, j = 0, m - 1
while i != n - 1 or j != 0:
    if i == n - 1:
        j -= 1
        path += "R"
    elif j == 0:
        i += 1
        path += "U"
    else:
        if dp[i + 1][j] > dp[i][j - 1]:
            i += 1
            path += "U"
        else:
            j -= 1
            path += "R"

print(path[::-1])

