# Read two input strings
import itertools
s1 = input().strip()
s2 = input().strip()

# Lengths of the strings
len1 = len(s1)
len2 = len(s2)

# Create a 2D DP table initialized with zeros
dp = []
dp.extend([0] * (len2 + 1) for _ in range(len1 + 1))
# Variable to store the length of the longest common substring
max_len = 0

# Fill the DP table
for i, j in itertools.product(range(1, len1 + 1), range(1, len2 + 1)):
    if s1[i-1] == s2[j-1]:  # Characters match
        dp[i][j] = dp[i-1][j-1] + 1
        if dp[i][j] > max_len:
            max_len = dp[i][j]

# Print the result
print(max_len)
