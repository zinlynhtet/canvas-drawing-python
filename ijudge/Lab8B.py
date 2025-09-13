# Read prices
prices_input = input().split()
prices = []
for x in prices_input:
    prices.append(float(x))

# Read amounts
amounts_input = input().split()
amounts = []
for x in amounts_input:
    amounts.append(int(x))

# Compute total cost
total = 0
for i in range(len(prices)):
    total += prices[i] * amounts[i]

# Print rounded to 2 decimal places
print("%.2f" % total)
