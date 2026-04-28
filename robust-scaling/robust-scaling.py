def robust_scaling(values):
    """
    Scale values using median and interquartile range.
    """
    val = values[:]
    val.sort()
    l = len(val)

    def median1(val):
        n = len(val)
        if n==0 :
            return 0 
        if n %2 != 0 :
            median = val[n//2]
        else : 
            median = (val[n//2-1] + val[n//2])/ 2
        return median

    median = median1(val)
    if l %2 == 0 :
        lower = val[:l//2]
        upper = val[l//2 :]
    else :
        lower = val[:l//2]
        upper = val[l//2 +1:]
        
    q1 = median1(lower)
    q3 = median1(upper)

    iqr = q3 - q1 if q3 != q1 else 1
    result = [(i-median)/iqr for i in values]

    return result