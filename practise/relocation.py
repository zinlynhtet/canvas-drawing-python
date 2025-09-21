n, q = map(int, input().split())

pos = [0] + list(map(int, input().split()))

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _, i, x = query
        pos[i] = x
    else:
        _, i, j = query
        print(abs(pos[i] - pos[j]))
