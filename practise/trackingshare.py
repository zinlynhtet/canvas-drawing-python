C = int(input().strip())
changes = {}

for _ in range(C):
    K = int(input().strip())
    records = []
    for _ in range(K):
        N, D = map(int, input().split())
        records.append((D, N))
    records.sort()
    
    prev = 0
    for day, shares in records:
        diff = shares - prev
        changes[day] = changes.get(day, 0) + diff
        prev = shares

days = sorted(changes.keys())
totals = []
current = 0
for d in days:
    current += changes[d]
    totals.append(current)

print(" ".join(map(str, totals)))
