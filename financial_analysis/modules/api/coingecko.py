import requests

def fetch_crypto_symbols():
    url = "https://api.coingecko.com/api/v3/coins/list"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return [coin['symbol'] for coin in data]
    else:
        print("🚫 خطا در دریافت اطلاعات از CoinGecko")
        return []