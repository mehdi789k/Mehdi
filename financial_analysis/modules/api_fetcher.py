import requests
from datetime import datetime
import jdatetime

def convert_to_persian(number):
    english_to_persian_digits = {
        '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴',
        '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹', ',': '،'
    }
    return ''.join(english_to_persian_digits.get(char, char) for char in str(number))

def fetch_dollar_price():
    """
    دریافت قیمت دلار از نوبیتکس و نمایش با فرمت مناسب به همراه زمان به‌روزرسانی و مدیریت خطا.
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
            # تاریخ شمسی
            shamsi = jdatetime.datetime.fromgregorian(datetime=now)
            shamsi_str = shamsi.strftime("%Y/%m/%d  %H:%M:%S")
            shamsi_persian = convert_to_persian(shamsi_str)
            print(f"💵 قیمت لحظه‌ای دلار (نوبیتکس): {price_persian} تومان")
            print(f"⏰ آخرین به‌روزرسانی (میلادی): {now_persian}")
            print(f"⏰ آخرین به‌روزرسانی (شمسی):  {shamsi_persian}")
        else:
            print("🚫 خطا در دریافت قیمت از سرور نوبیتکس.")
    except requests.exceptions.RequestException:
        print("🚫 خطا در اتصال به سرور نوبیتکس.")