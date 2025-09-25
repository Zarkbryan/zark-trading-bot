def sma(data, period):
    return sum(data[-period:]) / period if len(data) >= period else None

def ema(data, period):
    if len(data) < period:
        return None
    k = 2 / (period + 1)
    ema_current = sum(data[:period]) / period
    for price in data[period:]:
        ema_current = price * k + ema_current * (1 - k)
    return ema_current
