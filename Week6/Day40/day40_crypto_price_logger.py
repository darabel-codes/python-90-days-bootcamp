import requests
import time
from datetime import datetime

print("===== CRYPTO PRICE LOGGER =====")

def get_price(coin):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"
    
    try:
        #Go to the API → get data → convert it → extract the USD price of the coin
        response = requests.get(url) #Converts the response into Python format
        data = response.json() #Converts the response into Python format
        return data[coin]['usd']
    except:
        return None

coin = input("Enter your coin of choice (bitcoin, ethereum, solana e.t.c): ")

print(f"\nLogging {coin.upper()} prices... (Press CTRL + C to stop)")

while True:
    price = get_price(coin)
    
    if price:
        now = datetime.now().strftime("%Y %m %d %H:%M:%S")
       
        
        record = f"{now}, {coin}, ${price}\n"
        
        print(record.strip())
        
        with open("crypto_prices_log.csv", "a") as file:
            file.write(record)
            
    
    else:
        print("Error fetching price.")
        print("Retrying in 10 seconds...")
    
    time.sleep(10) #Wait 10 seconds before checking again   
    
         