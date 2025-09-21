t = int(input())
for _ in range(t):
    n = int(input())

    buy_orders = {}   # price -> shares
    sell_orders = {}  # price -> shares
    last_price = None

    for _ in range(n):
        parts = input().split()
        order_type = parts[0]
        shares = int(parts[1])
        price = int(parts[4])

        if order_type == "buy":
            buy_orders[price] = buy_orders.get(price, 0) + shares
        else:
            sell_orders[price] = sell_orders.get(price, 0) + shares

        # Try to match orders
        while buy_orders and sell_orders:
            best_bid = max(buy_orders.keys())
            best_ask = min(sell_orders.keys())
            if best_bid < best_ask:
                break

            qty = min(buy_orders[best_bid], sell_orders[best_ask])
            buy_orders[best_bid] -= qty
            sell_orders[best_ask] -= qty
            last_price = best_ask
            if buy_orders[best_bid] == 0:
                del buy_orders[best_bid]
            if sell_orders[best_ask] == 0:
                del sell_orders[best_ask]
        ask = min(sell_orders.keys()) if sell_orders else "-"
        bid = max(buy_orders.keys()) if buy_orders else "-"
        last = last_price if last_price is not None else "-"

        print(f"{ask} {bid} {last}")
