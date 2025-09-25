def moving_average(prices, window=14):
    return sum(prices[-window:]) / window if len(prices) >= window else None
