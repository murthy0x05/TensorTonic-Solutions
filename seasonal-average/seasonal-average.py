def seasonal_average(series: list, period: int) -> list:
    return [
        sum(series[i::period]) / len(series[i::period]) if series[i::period] else 0 
        for i in range(period)
    ]