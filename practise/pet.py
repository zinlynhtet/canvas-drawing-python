scores = []
for _ in range(5):
    # grades = list(map(int, input().split()))
    a = input().split()
    b = map(int, a)
    c = list(b)
    scores.append(sum(c))

max_points = max(scores)
winner = scores.index(max_points) + 1

print(winner, max_points)
