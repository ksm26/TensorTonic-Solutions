def differencing(series, order):
    """
    Apply d-th order differencing to the time series.
    """
    # Write code here
    def diff(series):
        result = []
        for i in range(1,len(series)):
            result.append(series[i]-series[i-1])

        return result

    new_series = []
        
    for i in range(order):
        new_series = diff(series)
        series = new_series

    return new_series
        

    