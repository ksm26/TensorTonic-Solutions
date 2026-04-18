def lag_features(series, lags):
    """
    Create a lag feature matrix from the time series.
    """
    # Write code here
    maxlag = max(lags)
    result = []
    
    for t in range(maxlag,len(series)):
        row = []
        for lag in lags:
            row.append(series[t-lag])
        result.append(row)

    return result