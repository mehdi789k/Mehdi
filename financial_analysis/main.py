import os
from modules.gui import display_welcome
from modules.api_fetcher import fetch_dollar_price
from modules.technical_analysis import analyze_market
from modules.trading_strategies import execute_trading_strategy
from modules.notifications import display_market_notifications

def main_menu():
    while True:
        print("\nمنوی اصلی:")
        print("1. نمایش قیمت دلار")
        print("2. تحلیل و آمار")
        print("3. اجرای تریدینگ هوشمند")
        print("4. اعلان‌های مهم بازار")
        print("5. خروج")
        
        choice = input("انتخاب شما: ")
        if choice == "1":
            fetch_dollar_price()
        elif choice == "2":
            analyze_market()
        elif choice == "3":
            execute_trading_strategy()
        elif choice == "4":
            display_market_notifications()
        elif choice == "5":
            print("خروج از برنامه...")
            backup_data()
            break
        else:
            print("انتخاب نامعتبر است، لطفاً دوباره تلاش کنید.")

def backup_data():
    print("در حال ذخیره‌سازی بکاپ...")
    # کد مربوط به ذخیره بکاپ

if __name__ == "__main__":
    display_welcome()
    main_menu()