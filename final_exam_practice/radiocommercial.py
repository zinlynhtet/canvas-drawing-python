n, p = map(int, input().split())
students = list(map(int, input().split()))

# Transform to net profit per break
net = [x - p for x in students]

max_profit = current = 0
for x in net:
    current = max(0, current + x)
    max_profit = max(max_profit, current)

print(max_profit)
