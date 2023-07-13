# Initialize dp array
dp = [[0] * 4 for _ in range(n + 1)]

# Initialize base cases
dp[1] = [1, 1, 1, 1]

# Calculate dp values
for i in range(2, n + 1):
    dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % MOD
    dp[i][2] = (dp[i - 1][1] + dp[i - 1][3]) % MOD
    dp[i][3] = (dp[i - 1][1] + dp[i - 1][2]) % MOD

# Calculate the final result
result = (dp[n][1] + dp[n][2] + dp[n][3]) % MOD

return result