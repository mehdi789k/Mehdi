# financial_analysis/modules/trading_strategies.py

from modules.analysis_tools import calculate_macd, calculate_rsi

def define_targets(data):
    """
    Defines three buy and sell targets based on analysis.
    """
    buy_targets = [data['close'][-1] * 1.02, data['close'][-1] * 1.04, data['close'][-1] * 1.06]
    sell_targets = [data['close'][-1] * 0.98, data['close'][-1] * 0.96, data['close'][-1] * 0.94]
    return buy_targets, sell_targets

def execute_trading_strategy(timeframe, data):
    """
    Executes a trading strategy based on the selected timeframe.
    """
    print(f"شروع تحلیل برای تایم‌فریم: {timeframe}")
    
    # Calculate indicators
    macd = calculate_macd(data)
    rsi = calculate_rsi(data)
    
    # Define buy/sell targets
    buy_targets, sell_targets = define_targets(data)

    # Display results
    print(f"MACD: {macd}")
    print(f"RSI: {rsi}")
    print("اهداف خرید:", buy_targets)
    print("اهداف فروش:", sell_targets)