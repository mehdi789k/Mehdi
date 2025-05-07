import matplotlib.pyplot as plt
import numpy as np

def calculate_macd():
    print("در حال محاسبه MACD...")
    data = np.random.randn(100)
    macd = np.convolve(data, np.ones(5)/5, mode='valid')
    print("MACD محاسبه شد:", macd)

def calculate_rsi():
    print("در حال محاسبه RSI...")
    data = np.random.randn(100)
    rsi = 100 - (100 / (1 + np.random.rand(len(data))))
    print("RSI محاسبه شد:", rsi)

def generate_reports():
    print("در حال تولید گزارش...")
    data = np.random.randn(100)
    plt.plot(data)
    plt.title("گزارش تحلیل بازار")
    plt.show()
    print("گزارش تولید شد.")