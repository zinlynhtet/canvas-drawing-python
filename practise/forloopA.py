# sourcery skip: while-to-for
for i in range(5):
    print(i, end=' ')
print()

for _ in range(5):
    for i in range(10):
        print(i, end=' ')
    print()
    
n = 5
while n > 0:
    for i in range(5):
        print(i, end=' ')
    print()
    n -= 1


n = 5
while n > 0:
    for i in range(n):
        print(i, end=' ')
    print()
    n -= 1