# Read input
prices = list(map(float, input().split()))
amounts = list(map(int, input().split()))

# Compute total cost
total = sum(p * a for p, a in zip(prices, amounts))

# Print rounded to 2 decimal places
print(f"{total:.2f}")
