import os
from modules.gui import display_welcome
from modules.api_fetcher import fetch_dollar_price
from modules.trading_strategies import execute_trading_strategy
from modules.notifications import display_market_notifications
from modules.analysis_tools import calculate_macd, calculate_rsi, generate_reports


def analyze_crypto_market():
    """
    تحلیل بازار مالی ارزدیجیتال.
    """
    print("\n=== تحلیل بازار مالی ارزدیجیتال ===")
    print("1. استراتژی 30 دقیقه‌ای")
    print("2. استراتژی 1 ساعته")
    print("3. استراتژی 4 ساعته")
    print("4. استراتژی روزانه")
    print("5. استراتژی هفتگی")
    print("6. استراتژی ماهانه")
    print("7. استراتژی سالانه")
    print("8. بازگشت به منوی اصلی")
    
    choice = input("لطفاً تایم‌فریم مورد نظر را انتخاب کنید: ")
    if choice == "8":
        print("بازگشت به منوی اصلی...")
        return
    elif choice in ["1", "2", "3", "4", "5", "6", "7"]:
        print(f"اجرای استراتژی برای تایم‌فریم: {choice}")
        # اجرای کد تحلیل مرتبط
    else:
        print("انتخاب نامعتبر. لطفاً دوباره تلاش کنید.")


def analyze_forex_market():
    """
    تحلیل بازار مالی فارکس.
    """
    print("\n=== تحلیل بازار مالی فارکس ===")
    print("1. استراتژی 30 دقیقه‌ای")
    print("2. استراتژی 1 ساعته")
    print("3. استراتژی 4 ساعته")
    print("4. استراتژی روزانه")
    print("5. استراتژی هفتگی")
    print("6. استراتژی ماهانه")
    print("7. استراتژی سالانه")
    print("8. بازگشت به منوی اصلی")
    
    choice = input("لطفاً تایم‌فریم مورد نظر را انتخاب کنید: ")
    if choice == "8":
        print("بازگشت به منوی اصلی...")
        return
    elif choice in ["1", "2", "3", "4", "5", "6", "7"]:
        print(f"اجرای استراتژی برای تایم‌فریم: {choice}")
        # اجرای کد تحلیل مرتبط
    else:
        print("انتخاب نامعتبر. لطفاً دوباره تلاش کنید.")


def analyze_market():
    """
    تحلیل و آمار بازار.
    """
    print("\n=== تحلیل و آمار بازار ===")
    print("1. بازار مالی ارزدیجیتال")
    print("2. بازار مالی فارکس")
    print("3. بازگشت به منوی اصلی")
    
    choice = input("لطفاً بازار مورد نظر را انتخاب کنید: ")
    if choice == "1":
        analyze_crypto_market()
    elif choice == "2":
        analyze_forex_market()
    elif choice == "3":
        print("بازگشت به منوی اصلی...")
    else:
        print("انتخاب نامعتبر. لطفاً دوباره تلاش کنید.")


def main_menu():
    while True:
        print("\nمنوی اصلی:")
        print("1. نمایش قیمت دلار")
        print("2. تحلیل و آمار بازار")
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