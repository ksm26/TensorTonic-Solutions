def percent_change(series):
    """
    Compute the fractional change between consecutive values.
    """
    result = []

    for i in range(len(series)-1):
        if series[i] != 0 :
            result.append((series[i+1]-series[i])/series[i])
        else : 
            result.append(0.0)
    return result