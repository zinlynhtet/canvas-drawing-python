n,k,d = map(int,input().split())
colors = sorted(map(int,input().split()))
loads = 0
i = 0
for _ in range(n):
    if i >= n:
        break
    loads += 1
    start = colors[i]
    count_sock = 0
    for j in range(i, n):
        if count_sock == k or colors[j] - start > d:
            break
        count_sock += 1
        i += 1

print(loads)