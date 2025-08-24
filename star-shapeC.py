def starshapeC(n):
    if n == 0:
        return

    def helper(current, target):
        if current > target:
            return
        print_spaces(target - current)
        print_stars(current)
        print()
        helper(current + 1, target)

    def print_spaces(k):
        if k == 0:
            return
        print(' ', end='')
        print_spaces(k - 1)

    def print_stars(k):
        if k == 0:
            return
        print('*', end='')
        print_stars(k - 1)

    helper(1, n)
    
for n in [0,1,2,3,4,5,10]:
  print(n)
  starshapeC(n)