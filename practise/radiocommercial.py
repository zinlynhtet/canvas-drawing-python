
# sourcery skip: min-max-identity
n, price = map(int,input().split())
students = map(int,input().split())

stu =  list(students)

net = [s - price for s in stu]
maxi = 0
current = 0
for p in net:
    current += p
    if current < 0:
        current = 0 
    if current > maxi:
        maxi = current

print(maxi)