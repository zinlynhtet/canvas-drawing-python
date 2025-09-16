exchange_rates = {
    "USD": 1.0,
    "EUR": 0.957,
    "GBP": 1.0,
    "JPY": 110.0,
    "THB": 33.0,
    "SGD": 1.35,
    "AUD": 1.45,
    "CNY": 6.45,
}

from_currency = input().strip().upper()
amount = float(input().strip())
to_currency = input().strip().upper()

amount_in_usd = amount / exchange_rates[from_currency]
result = amount_in_usd * exchange_rates[to_currency]

print(f"{result:.2f}")
