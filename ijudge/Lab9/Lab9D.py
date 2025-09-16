exchange_rates = {
    "THB_TO": {
        "GBP": 1 / 43.3,
        "USD": 1 / 34.5,
        "EUR": 1 / 41.7,
        "JPY": 1 / 0.41,
        "SGD": 1 / 29.6,
        "AUD": 1 / 28.9,
        "CNY": 1 / 5.2,
    },
    "TO_THB": {
        "GBP": 39.9,
        "USD": 31.2,
        "EUR": 40.0,
        "JPY": 0.33,
        "SGD": 28.5,
        "AUD": 26.2,
        "CNY": 4.4,
    }
}

def convert_currency(from_currency, amount, to_currency):
    if from_currency == "THB" and to_currency != "THB":
        converted_amount = amount * exchange_rates["THB_TO"][to_currency]
    elif to_currency == "THB" and from_currency != "THB":
        converted_amount = amount * exchange_rates["TO_THB"][from_currency]
    else:  
        amount_in_thb = amount * exchange_rates["TO_THB"][from_currency]
        converted_amount = amount_in_thb * exchange_rates["THB_TO"][to_currency]
    return round(converted_amount, 2)

from_currency = input().strip().upper()
amount = float(input().strip())
to_currency = input().strip().upper()

result = convert_currency(from_currency, amount, to_currency)
print(f"{result:.2f}")
