def autocorrelation(series, max_lag):
    """
    Compute the autocorrelation of a time series for lags 0 to max_lag.
    """
    n = len(series)

    mean = sum(series)/n
    var = sum((x-mean)**2 for x in series)
    result = []
    if var == 0:
        return [1.0] + [0.0] * max_lag

    for k in range(max_lag+1):
        count = 0 
        for t in range(n-k):
            count += (series[t]-mean) *(series[t+k]-mean)

        result.append(count / var)

    return result 