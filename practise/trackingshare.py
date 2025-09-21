# C = int(input().strip())
# changes = {}

# for _ in range(C):
#     K = int(input().strip())
#     records = []
#     for _ in range(K):
#         N, D = map(int, input().split())
#         records.append((D, N))
#     records.sort()

#     prev = 0
#     for day, shares in records:
#         diff = shares - prev
#         changes[day] = changes.get(day, 0) + diff
#         prev = shares

# days = sorted(changes.keys())
# totals = []
# current = 0
# for d in days:
#     current += changes[d]
#     totals.append(current)

# print(" ".join(map(str, totals)))

c = int(input().strip())

if not 1 <= c <= 20:
    print("Invalid company numbers")
else:
    changes = {}
    for _ in range(c):
        k = int(input().strip())
        if not 1 <= k <= 50:
            print("Invalid record numbers")
        else:
            records = []
            for _ in range(k):
                n, d = map(int, input().split())
                if not (0 <= n <= 1000) or not (1 <= d <= 365):
                    print("Invalid share or day numbers")
                else:
                    records.append((d, n))

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
