import requests
import time

print("===== CRYPTO PRICE TRACER =====")


def get_price(coin):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    
    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if coin in data:
            return data[coin]['usd']
        else:
            return None

    except requests.exceptions.RequestException:
        print("⚠️ Network error while fetching crypto price.")
        return None


def get_exchange_rate():
    url = "https://v6.exchangerate-api.com/v6/e78ab4ef365a8ef64220c56c/latest/USD"
    
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        return data['conversion_rates']['NGN']

    except requests.exceptions.RequestException:
        print("⚠️ Network error while fetching exchange rate.")
        return None


exchange_rate = get_exchange_rate()

if exchange_rate:
    print(f"Current USD → NGN rate: ₦{exchange_rate:.2f}")
else:
    print("⚠️ Could not fetch exchange rate. Naira conversion disabled.")

while True:
    coin = input("\nEnter coin (bitcoin, ethereum, etc): ").lower().strip()
    
    price = get_price(coin)

    if price:
        print(f"\n💰 {coin.upper()} Price:")
        print(f"USD: ${price}")

        if exchange_rate:
            naira_amount = price * exchange_rate
            print(f"NGN: ₦{naira_amount:,.2f}")
    else:
        print("❌ Coin not found. Use full name like 'bitcoin', not 'btc'.")

    again = input("\nCheck another coin? (y/n): ").lower()
    if again != 'y':
        print("Goodbye!")
        break

    time.sleep(2)