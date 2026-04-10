import requests
import time

print("==== CRYPTO ALERT BOT ====")


def get_price(coin):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"

    try:
        response = requests.get(url)
        data = response.json()
        return data[coin]["usd"]
    except:
        return None


coin = input("Enter coin (bitcoin, ethereum): ").lower()
target_price = float(input("Enter target price (USD): "))

print(f"\nTracking {coin.upper()}...")

while True:
    price = get_price(coin)

    if price:
        print(f"Current price: ${price}")

        if price >= target_price:
            print("🚨 TARGET REACHED! SELL OR TAKE ACTION!")
            break

    else:
        print("Error fetching price.")

    time.sleep(10)  # wait 10 seconds before checking again