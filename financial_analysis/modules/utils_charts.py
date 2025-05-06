import matplotlib.pyplot as plt
import pandas as pd

def plot_candlestick_chart():
    # داده‌های نمونه (Open, High, Low, Close)
    data = {
        "timestamp": ["2023-01-01", "2023-01-02", "2023-01-03"],
        "open": [100, 105, 102],
        "high": [110, 108, 107],
        "low": [99, 102, 101],
        "close": [108, 104, 106],
    }
    df = pd.DataFrame(data)

    # رسم نمودار
    plt.figure(figsize=(10, 5))
    plt.plot(df['timestamp'], df['close'], marker='o', label='Close Price')
    plt.title("نمودار کندل‌استیک")
    plt.legend()
    plt.show()