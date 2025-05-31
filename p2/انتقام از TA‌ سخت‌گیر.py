n = int(input())

dp = [0 for _ in range(25)]
dp[0] = 1
dp[1] = 0
dp[2] = 3
dp[3] = 0
# if n is odd there is gap ant the answer is 0
for i in range(4, n + 1):
    dp[i] = 4 * dp[i - 2] - dp[i - 4]

print(dp[n] * 2)