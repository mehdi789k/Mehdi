import requests

def convert_to_persian(number):
    """
    Convert English digits in a string to Persian digits.
    """
    english_to_persian_digits = {
        '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴',
        '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹'
    }
    return ''.join(english_to_persian_digits.get(char, char) for char in str(number))

def fetch_usdt_price():
    """
    Fetch the latest price of USDT in IRR from Nobitex API.
    """
    url = "https://api.nobitex.ir/market/stats"
    params = {
        "srcCurrency": "usdt",  # نماد تتر
        "dstCurrency": "rls"   # نماد ریال ایران
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # بررسی خطاهای HTTP
        
        data = response.json()
        if "stats" in data and "usdt-rls" in data["stats"]:
            price = data["stats"]["usdt-rls"]["latest"]
            return convert_to_persian(price)
        else:
            return "خطا در دریافت قیمت"
    except requests.exceptions.RequestException:
        return "خطا در اتصال به سرور"