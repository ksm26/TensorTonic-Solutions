def seasonal_average(series, period):
    """
    Compute the average value for each position in the seasonal cycle.
    """
    n = len(series)
    p = int(n/period)
    seasonal_out = []

    for i in range(period):
        row = []
        j = i 
        while j < n : 
            row.append(series[j])
            j += period

        seasonal_out.append(sum(row)/len(row))

    return seasonal_out
        
            