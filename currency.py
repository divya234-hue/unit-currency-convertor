rates = {
    "INR": 1,
    "USD": 0.0119,
    "EUR": 0.0102,
    "GBP": 0.0088,
    "JPY": 1.76,
    "AUD": 0.0181,
    "CAD": 0.0161
}


def currency_converter(amount, from_currency, to_currency):
    if from_currency not in rates:
        return "Invalid source currency"

    if to_currency not in rates:
        return "Invalid target currency"
    amount_in_inr = amount / rates[from_currency]
    result = amount_in_inr * rates[to_currency]

    return result