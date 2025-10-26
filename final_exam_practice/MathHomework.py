l1, l2, l3, L = map(int, input().split())

solutions = []

for a1 in range(L // l1 + 1):
    for a2 in range((L - l1 * a1) // l2 + 1):
        remaining = L - l1 * a1 - l2 * a2
        if remaining >= 0 and remaining % l3 == 0:
            a3 = remaining // l3
            solutions.append((a1, a2, a3))

if not solutions:
    print("impossible")
else:
    for sol in solutions:
        print(sol[0], sol[1], sol[2])
