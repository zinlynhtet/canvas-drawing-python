n = int(input().strip())

common = set(input().split())

for _ in range(n - 1):
    favorites = set(input().split())
    common &= favorites  

if common:
    print(" ".join(sorted(common)))
else:
    print("Nothing")
