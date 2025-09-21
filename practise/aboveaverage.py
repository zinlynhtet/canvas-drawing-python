t = int(input())

for _ in range(t):
    data = list(map(int, input().split()))
    n = data[0]
    grades = data[1:]     

    while len(grades) < n:
        grades.extend(map(int, input().split()))

    avg = sum(grades) / n
    above_avg = sum(1 for g in grades if g > avg)

    percent = (above_avg / n) * 100
    print(f"{percent:.3f}%")
