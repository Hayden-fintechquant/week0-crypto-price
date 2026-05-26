import requests
import json

def get_cyrpto_price(coin_id):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": coin_id,
        "vs_currencies": "usd"
    }
    response = requests.get(url, params=params)
    data = response.json()
    price = data[coin_id]["usd"]
    return price

def save_to_file(coin_id, price):
    # Step 1 — create a Python dictionary
    result = {"coin": coin_id, "price": price}

    # Step 2 — write it to a JSON file
    with open ("prices.json", "w") as f:
        json.dump(result, f, indent=4)

    print(f"Saved to prices.json")

coin = "ethereum"
price = get_cyrpto_price(coin)
print(f"Current {coin} price: ${price:,.2f}")
save_to_file(coin, price)
    

