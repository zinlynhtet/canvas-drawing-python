def solve_pizza_order():
    n = int(input())
    prices = []
    
    for _ in range(n):
        line = input().split()
        # Last element is the price, everything before is the pizza name
        price = int(line[-1])
        prices.append(price)
    
    # Sort prices in descending order
    prices.sort(reverse=True)
    
    # Pair up pizzas: pay for every other pizza starting from index 0
    # When buying 2 pizzas, we only pay for the more expensive one
    total_cost = 0
    for i in range(0, n, 2):
        # We always pay for the pizza at even indices (0, 2, 4, ...)
        # because these are the more expensive ones in each pair
        total_cost += prices[i]
    
    print(total_cost)

if __name__ == "__main__":
    solve_pizza_order()
