from modules.search import search_symbols
from modules.analysis.crypto import crypto_analysis
from modules.analysis.forex import forex_analysis
from modules.analysis.stocks import stocks_analysis
from modules.analysis.metals import metals_analysis
from modules.trading import trading_menu
from modules.notifications import notifications_menu

def main_menu():
    while True:
        print("\n=== منوی اصلی ===")
        print("1. جستجو و اطلاعات اولیه نمادها")
        print("2. تحلیل بازار مالی ارز دیجیتال")
        print("3. تحلیل بازار مالی فارکس")
        print("4. تحلیل بازار مالی سهام")
        print("5. تحلیل بازار مالی فلزات")
        print("6. تریدینگ")
        print("7. اعلان‌های مهم بازار")
        print("8. خروج")

        choice = input("لطفاً گزینه مورد نظر را انتخاب کنید: ")

        if choice == "1":
            search_symbols()
        elif choice == "2":
            crypto_analysis()
        elif choice == "3":
            forex_analysis()
        elif choice == "4":
            stocks_analysis()
        elif choice == "5":
            metals_analysis()
        elif choice == "6":
            trading_menu()
        elif choice == "7":
            notifications_menu()
        elif choice == "8":
            print("خدانگهدار! 🌟")
            break
        else:
            print("🚫 انتخاب نامعتبر. لطفاً دوباره تلاش کنید!")