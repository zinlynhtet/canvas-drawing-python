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
    
for j in range(10):
    print("Line:", j, end=': ')
    for i in range(j+1):
        print(i, end=' ')
    print()

while True:
    s = input("Enter your user name:").strip()
    if s == "":  # empty string
        break
    print("Hello", s)
print("Done")