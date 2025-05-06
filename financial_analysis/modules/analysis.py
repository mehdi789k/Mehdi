from modules.utils.charts import plot_candlestick_chart
import pandas as pd

def crypto_analysis():
    print("در حال تحلیل بازار ارز دیجیتال...")

    # داده‌های نمونه
    data = pd.DataFrame({
        'timestamp': ['2025-04-25', '2025-04-26', '2025-04-27'],
        'open': [100, 105, 102],
        'high': [110, 108, 107],
        'low': [99, 102, 101],
        'close': [108, 104, 106]
    })

    # رسم نمودار
    plot_candlestick_chart(data)