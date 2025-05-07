import requests

def fetch_forex_symbols():
    """
    Fetch a list of Forex symbols from Yahoo Finance.
    Returns:
        List of Forex symbols.
    """
    # نمونه کد برای دریافت داده‌های فارکس (می‌توانید این را با API واقعی جایگزین کنید)
    url = "https://query1.finance.yahoo.com/v7/finance/spark"
    params = {
        "symbols": "EURUSD=X,USDJPY=X,GBPUSD=X",  # نمادهای فارکس
        "range": "1d",
        "interval": "1m"
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return list(data['spark']['result'][0]['response'].keys())
    else:
        print("🚫 خطا در دریافت اطلاعات از Yahoo Finance")
        return []