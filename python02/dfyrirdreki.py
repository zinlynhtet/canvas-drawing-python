a = int(input())
b = int(input())
c = int(input())

discriminant = b**2 - 4*a*c

if discriminant > 0:
    print(2)
elif discriminant == 0:
    print(1)
else:
    print(0)

# ax^2 + bx + c = 0 (a!=0)
# x = (-b ± √(b² - 4ac)) / 2a
# D = b² - 4ac
# The term inside the square root is the discriminant.
