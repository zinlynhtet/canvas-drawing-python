# Read field size
n = int(input())
m = int(input())

# Read the field
field = []
for _ in range(n):
    field.append(list(input().strip()))

# Check each cell
for i in range(n):
    for j in range(m):
        if field[i][j] == '-':
            count = 0
            # Check 8 neighbors
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < m:
                        if field[ni][nj] == '*':
                            count += 1
            field[i][j] = str(count)

# Print the result
for row in field:
    print("".join(row))
