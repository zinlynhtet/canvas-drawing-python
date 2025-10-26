n, v = map(int, input().split())
lines = [int(input()) for _ in range(n)]

lines.sort()
total_lines = 0
count = 0
limit = 5 * v

for l in lines:
    if total_lines + l <= limit:
        total_lines += l
        count += 1
    else:
        break

print(count)
