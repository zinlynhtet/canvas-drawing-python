n = int(input())
values = list(map(int, input().split()))

total_expenses = sum(-x for x in values if x < 0)
print(total_expenses)
