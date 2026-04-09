import requests

print("===== CRYPTO DASHBOARD =====")

def get_crypto_data(coin):
    url = f"https://api.coingecko.com/api/v3/coins/{coin}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        market = data["market_data"]
        
        return {
            "name": data["name"],
            "price": market["current_price"]["usd"],
            "high_24h": market["high_24h"]["usd"],
            "low_24h": market["low_24h"]["usd"],
            "market_cap": market["market_cap"]["usd"]   
        }
    except:
        return None
    
while True:
    coin = input("\nEnter coin (bitcoin, ethereum): ").lower()
    info = get_crypto_data(coin)

    if info:
        
        print(f"\n--- {info['name']} ---")
        print(f"Price: ${info['price']}")
        print(f"24h High: ${info['high_24h']}")
        print(f"24h Low: ${info['low_24h']}")
        print(f"Market Cap: ${info['market_cap']:,}")
        
    else:
        print("Error fetching data.")

    again = input("\nCheck another coin? (y/n): ").lower()
    if again != "y":
        break