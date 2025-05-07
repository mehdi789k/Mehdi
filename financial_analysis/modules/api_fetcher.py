import requests
from datetime import datetime
import jdatetime


def convert_to_persian(number):
    """
    Converts English digits to Persian digits.
    """
    english_to_persian_digits = {
        '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴',
        '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹', ',': '،'
    }
    return ''.join(english_to_persian_digits.get(char, char) for char in str(number))


def fetch_dollar_price():
    """
    Fetches the current dollar price from Nobitex and displays it in Persian format
    along with the last update time in Gregorian and Jalali calendars.
    """
    url = "https://api.nobitex.ir/market/stats"
    params = {
        "srcCurrency": "usdt",
        "dstCurrency": "rls"
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        if "stats" in data and "usdt-rls" in data["stats"]:
            price = data["stats"]["usdt-rls"]["latest"]
            price_str = f"{int(float(price)):,}"
            price_persian = convert_to_persian(price_str)

            now = datetime.now()
            now_str = now.strftime("%Y/%m/%d  %H:%M:%S")
            now_persian = convert_to_persian(now_str)

            # Convert to Jalali date
            shamsi = jdatetime.datetime.fromgregorian(datetime=now)
            shamsi_str = shamsi.strftime("%Y/%m/%d  %H:%M:%S")
            shamsi_persian = convert_to_persian(shamsi_str)

            print(f"💵 قیمت لحظه‌ای دلار (نوبیتکس): {price_persian} تومان")
            print(f"⏰ آخرین به‌روزرسانی (میلادی): {now_persian}")
            print(f"⏰ آخرین به‌روزرسانی (شمسی):  {shamsi_persian}")
        else:
            print("🚫 خطا در دریافت قیمت از سرور نوبیتکس.")
    except requests.exceptions.RequestException as e:
        print("🚫 خطا در اتصال به سرور نوبیتکس.")
        print(f"🔍 جزئیات خطا: {e}")


def fetch_crypto_data(symbol):
    """
    Fetches cryptocurrency market data from the CoinGecko API.
    """
    url = f"https://api.coingecko.com/api/v3/coins/{symbol}/market_chart"
    params = {'vs_currency': 'usd', 'days': '90', 'interval': 'hourly'}
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"🚫 خطا در دریافت داده‌های ارز دیجیتال برای {symbol}.")
        print(f"🔍 جزئیات خطا: {e}")
        return None


def fetch_forex_data(symbol):
    """
    Fetches Forex market data using Yahoo Finance API.
    """
    url = f"https://query1.finance.yahoo.com/v7/finance/chart/{symbol}"
    params = {'range': '1mo', 'interval': '1h'}
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"🚫 خطا در دریافت داده‌های فارکس برای {symbol}.")
        print(f"🔍 جزئیات خطا: {e}")
        return None