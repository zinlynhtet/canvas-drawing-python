n = int(input())
#ALY (Quality-Adjusted Life Years), 
#which is computed as the sum of each period's quality of life multiplied by the number of years.
total = 0.0
for _ in range(n):
    q, y = map(float, input().split())
    total += q * y
    
print(f"{total:.3f}")
    