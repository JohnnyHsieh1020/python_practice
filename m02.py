def fee(isDiscount, minutes):
    total = 0

    if isDiscount:
        print('減價時段, 分鐘數{minutes}'.format(
            isDiscount=isDiscount, minutes=minutes))
        total = 300 * (minutes // 60) + 6 * (minutes % 60)
        return format(total, ',')
    else:
        print('非減價時段, 分鐘數{minutes}'.format(
            isDiscount=isDiscount, minutes=minutes))
        total = 480 * (minutes // 60) + 9 * (minutes % 60)
        return format(total, ',')
