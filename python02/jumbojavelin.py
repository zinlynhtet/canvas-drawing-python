n = int(input())
total_length = 0

for _ in range(n):
    rod = int(input())
    total_length += rod

fused_length = total_length - (n - 1)
print(fused_length)
