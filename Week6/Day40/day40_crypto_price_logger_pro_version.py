import requests
import time
from datetime import datetime

def get_price(coin):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    try:
        response = requests.get(url)
        data = response.json()
        return data[coin]["usd"]
    except:
        return None


def get_usd_to_ngn():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    try:
        return requests.get(url).json()["rates"]["NGN"]
    except:
        return None


coins = input("Enter coins (comma separated): ").lower().split(",")
coins = [c.strip() for c in coins]

previous_prices = {}

while True:
    rate = get_usd_to_ngn()

    for coin in coins:
        price = get_price(coin)

        if price:
            prev = previous_prices.get(coin)
            now = datetime.now().strftime("%Y %m %d %H:%M:%S")

            print(f"\n--- {coin.upper()} ---")

            if prev:
                change = price - prev
                symbol = "📈" if change > 0 else "📉"
                print(f"{symbol} Change: ${change:.2f}")

            record = f"{now}, {coin}, USD:, ${price}\n"
            print(record.strip())
            

            if rate:
                print(f"NGN: ₦{price * rate:,.2f}")

            previous_prices[coin] = price

            
            with open("crypto_prices_log.csv", "a") as file:
                file.write(record)  
       
        else:
            print(f"{coin} not found.")

    print("\nRefreshing...\n")
    time.sleep(10)