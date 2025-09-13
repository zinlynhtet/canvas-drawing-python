numbers = []

while True:
    line = input().strip()
    if line == "$":
        break
    numbers.append(int(line))

n = len(numbers)

mean = sum(numbers) / n

variance = sum((x - mean) ** 2 for x in numbers) / n

std_dev = variance ** 0.5

print(f"{std_dev:.2f}")
