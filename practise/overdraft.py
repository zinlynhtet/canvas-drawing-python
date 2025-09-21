n = int(input())
balance = 0
min_balance = 0

for _ in range(n):
    x = int(input())
    balance += x
    min_balance = min(min_balance, balance)

print(-min_balance)
