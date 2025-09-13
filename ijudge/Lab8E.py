# Read input coefficients
p = list(map(int, input().split()))
q = list(map(int, input().split()))

# Initialize result list with zeros
m = len(p)
n = len(q)
result = [0] * (m + n - 1)

# Multiply polynomials
for i in range(m):
    for j in range(n):
        result[i + j] += p[i] * q[j]

# Print result
print(' '.join(map(str, result)))
