T = int(input())

for _ in range(T):
    seq = list(map(int, input().split()))
    imports = 0
    
    for i in range(1, len(seq)-1):  # ignore last 0
        if seq[i] > 2 * seq[i-1]:
            imports += seq[i] - 2 * seq[i-1]
    
    print(imports)
