from modules.api.coingecko import fetch_crypto_symbols
from modules.api.yahoo_finance import fetch_forex_symbols

def search_symbols():
    print("\n=== جستجو و اطلاعات اولیه نمادها ===")
    market = input("بازار مورد نظر (ارز دیجیتال/فارکس): ").strip().lower()

    if market == "ارز دیجیتال":
        symbols = fetch_crypto_symbols()
    elif market == "فارکس":
        symbols = fetch_forex_symbols()
    else:
        print("🚫 بازار نامعتبر. لطفاً دوباره تلاش کنید!")
        return

    query = input("بخشی از نماد را وارد کنید: ").strip().lower()
    matched_symbols = [s for s in symbols if query in s.lower()]

    print("\nنمادهای مرتبط:")
    for symbol in matched_symbols:
        print(f"- {symbol}")