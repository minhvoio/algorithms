# https://judge.monashaps.com/problem/formula

# a, b, k = map(int, input().split())

# def formula(a: int, b: int, k: int):
#   if k == 0:
#     return a
#   elif k == 1:
#     return b

#   if k in memo:
#     return memo[k]%mod

#   ans = a*formula(a, b, k-1) + b*formula(a, b, k-2)
#   memo[k] = ans

#   return ans%mod

# print(formula(a, b, k))

a, b, k = [int(x) for x in input().split()]

mod = 1000000007

memo = dict()

dp = [0 for _ in range(k+1)]

dp[0] = a
dp[1] = b

for i in range(2, k+1):
  dp[i] = dp[i-1]*a + dp[i-2]*b
  dp[i] %= mod

print(dp[k])