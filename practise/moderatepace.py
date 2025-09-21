n = int(input())
you = list(map(int, input().split()))
col1 = list(map(int, input().split()))
col2 = list(map(int, input().split()))

plan = []

for i in range(n):
    day_choices = [you[i], col1[i], col2[i]]
    day_choices.sort()
    plan.append(day_choices[1])  

print(" ".join(map(str, plan)))
