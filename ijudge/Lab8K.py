s1 = input().strip()
s2 = input().strip()

# Create a 2D DP table
dp = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]
max_len = 0

for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            max_len = max(max_len, dp[i][j])

print(max_len)
