def print_stars(k):
    if k == 0:
        return
    print('*', end='')  
    print_stars(k - 1)

def starshapeB(n):
    def helper(a, b):
        if a > b:
            return
        print_stars(a)
        print()
        helper(a + 1, b)

    helper(1, n)