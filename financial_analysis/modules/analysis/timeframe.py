# financial_analysis/modules/analysis/timeframe.py

def get_timeframes():
    """
    Returns a list of available timeframes.
    """
    return [
        "1 ساعت", "4 ساعت", "روزانه", "هفتگی", "ماهانه", "سالانه"
    ]

def validate_timeframe(choice):
    """
    Validates the user's choice of timeframe.
    """
    timeframes = get_timeframes()
    if choice.isdigit() and 1 <= int(choice) <= len(timeframes):
        return timeframes[int(choice) - 1]
    else:
        return None