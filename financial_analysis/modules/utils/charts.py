import matplotlib.pyplot as plt
import pandas as pd

def plot_candlestick_chart(data):
    """
    رسم نمودار کندل‌استیک.
    داده‌ها باید شامل ستون‌های 'timestamp', 'open', 'high', 'low' و 'close' باشد.
    """
    # بررسی داده‌ها
    if not all(col in data.columns for col in ['timestamp', 'open', 'high', 'low', 'close']):
        raise ValueError("داده‌ها باید شامل ستون‌های 'timestamp', 'open', 'high', 'low' و 'close' باشند.")

    # تنظیم فرمت تاریخ
    data['timestamp'] = pd.to_datetime(data['timestamp'])

    # رسم نمودار کندل‌استیک
    plt.figure(figsize=(12, 6))
    for index, row in data.iterrows():
        color = 'green' if row['close'] >= row['open'] else 'red'
        plt.plot([index, index], [row['low'], row['high']], color='black')  # سایه
        plt.plot([index, index], [row['open'], row['close']], color=color, linewidth=6)  # بدنه کندل

    plt.title("نمودار کندل‌استیک")
    plt.xlabel("زمان")
    plt.ylabel("قیمت")
    plt.show()