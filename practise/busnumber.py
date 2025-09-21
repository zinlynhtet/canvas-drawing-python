n = int(input())
buses = sorted(map(int, input().split()))

result = []
i = 0

for i in range(n):
    if i == 0 or buses[i] != buses[i-1] + 1:
        start = buses[i]
    
    if i == n-1 or buses[i+1] != buses[i] + 1:
        end = buses[i]
        length = end - start + 1
        if length >= 3:
            result.append(f"{start}-{end}")
        else:
            for x in range(start, end+1):
                result.append(str(x))

print(" ".join(result))
