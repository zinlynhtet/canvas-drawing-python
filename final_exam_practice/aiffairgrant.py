n = int(input())
prices = [int(input()) for _ in range(n)]

max_price = max(prices)
min_price = min(prices)

reimbursement_limit = max_price / 2
reimbursement = min(min_price, reimbursement_limit)

net_cost = min_price - reimbursement
print(int(net_cost))
