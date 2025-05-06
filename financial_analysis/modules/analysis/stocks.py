def stocks_analysis():
    """
    تحلیل بازار مالی سهام
    """
    print("\n=== تحلیل بازار مالی سهام ===")
    print("تایم‌فریم‌ها:")
    timeframes = ["5 دقیقه", "30 دقیقه", "1 ساعت", "4 ساعت", "6 ساعت", "12 ساعت", "روزانه", "هفتگی", "ماهانه", "سالیانه"]
    for i, tf in enumerate(timeframes, 1):
        print(f"{i}. {tf}")

    choice = input("لطفاً تایم‌فریم مورد نظر را انتخاب کنید: ")
    if choice.isdigit() and 1 <= int(choice) <= len(timeframes):
        print(f"شما تایم‌فریم {timeframes[int(choice) - 1]} را انتخاب کردید.")
        # تحلیل مرتبط با تایم‌فریم اجرا شود
    else:
        print("🚫 انتخاب نامعتبر. لطفاً دوباره تلاش کنید!")