# This program will convert the exchange rate from USD to EUR and vice versa.

import requests

print("===== EXCHANGE RATE CHECKER =====")

# Get the exchange rate from an API
url = "https://api.exchangerate-api.com/v4/latest/USD"

try:
    response = requests.get(url)
    data = response.json()
    exchange_rates = data["rates"]
    
    # print("\nAvailable currencies example: NGN, EUR, GBP")
    base_currency = input("From currency: ").upper()
    
    quote_currency = input("To currency: ").upper()
    
    if (base_currency and quote_currency) in exchange_rates:
        amount = float(input(f"Enter amount in {base_currency}: "))
        usd_amount = amount / exchange_rates[base_currency]
        converted = usd_amount * exchange_rates[quote_currency]
        print(f"\n{amount} {base_currency} = {converted:.2f} {quote_currency}.")
    else:
        print("Currency not found.")
except requests.exceptions.RequestException as error:
    print("Error fetching exchange rates:", error)