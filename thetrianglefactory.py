a = int(input())
b = int(input())
c = int(input())

if a == 90 or b == 90 or c == 90:
    print("Ratvinklig Triangel")
elif a > 90 or b > 90 or c > 90:
    print("Trubbig Triangel")
else:
    print("Spetsig Triangel")

