n = int(input())

count = 0
x = 1

while x * (x + 1) * (x + 2) < n:
    count += 1
    x += 1

print(count)
