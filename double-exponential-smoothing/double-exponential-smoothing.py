def double_exponential_smoothing(series, alpha, beta):
    """
    Apply Holt's linear trend method and return the level values.
    """
    level = series[0]
    output = [series[0]]
    trend = series[1] - series[0]

    for j in range(1,len(series)):
        new_level = alpha *series[j] + (1-alpha) * (level + trend)
        new_trend = beta * (new_level - level) + (1-beta)*trend

        output.append(new_level)
        level = new_level
        trend = new_trend

    return output
        
        
        
        