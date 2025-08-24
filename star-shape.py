def print_stars(k):
    if k == 0:
        return
    print('*', end='')
    print_stars(k - 1)
    
def starshapeA(n):
    if n == 0:
        return
    print_stars(n)
    print()
    starshapeA(n - 1)
    
for n in [0,1,2,3,4,5,10]:
  print(n)
  starshapeA(n)