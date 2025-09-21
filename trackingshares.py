class ErrorMessages:
    INVALID_COMPANIES = "The numbers of companies are invalid"
    INVALID_BLOCKS = "The numbers of blocks are invalid"
    INVALID_SHARES_OR_DAYS = "The numbers of shares or days are invalid"

c = int(input().strip())
if not (1 <= c <= 20):
    print(ErrorMessages.INVALID_COMPANIES)
else:
    changes = {}
    for _ in range(c):
        k = int(input().strip())
        if not (1 <= k <= 50):
            print(ErrorMessages.INVALID_BLOCKS)
        else:
            records = []
            for _ in range(k):
                n,d = map(int, input().split())
                if not (1 <= n <= 1000 and 1 <= d <= 365):
                    print(ErrorMessages.INVALID_SHARES_OR_DAYS)
                else:
                    records.append((d,n))
            records.sort()
            prev = 0
            for day, shares in records:
                diff = shares - prev
                changes[day] = changes.get(day, 0) + diff
                prev = shares
    days = sorted(changes.keys())
    total  =[]
    current = 0
    for d in days:
        current += changes[d]
        total.append(current)
    print(" ".join(map(str, total)))
    