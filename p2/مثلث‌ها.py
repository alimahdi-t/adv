t = int(input())

for _ in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    # print(arr)
    dp = [[arr[i][j] if i == 0 else 0 for j in range(i + 1)] for i in range(0, n + 1)]
    # print(dp)
    # dp[0][0] = arr[0][0]
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + arr[i][0]
        dp[i][i] = dp[i - 1][i - 1] + arr[i][i]
    for i in range(2, n):
        for j in range(1, i):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + arr[i][j]

    print(max(dp[n - 1]))



