n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# print your output
dp = [[0]*(n+1) for _ in range(n+1)]

dp[1][1] = 1

for i in range(n):
  for j in range(n):
    dp[i + a[i][j]][j] += dp[i][j]
    dp[i][j + a[i][j]] += dp[i][j]

