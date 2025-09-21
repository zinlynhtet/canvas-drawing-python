numbers = []

while True:
    line = input().strip()
    if line == "$":
        break
    numbers.append(int(line))

numbers.sort()
n = len(numbers)

if n % 2 == 1:
    median = numbers[n // 2]
else:
    median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2

print(f"{median:.1f}")
