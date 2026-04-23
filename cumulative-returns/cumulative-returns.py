def cumulative_returns(returns):
    """
    Compute the cumulative return at each time step.
    """
    result = []
    curr = 1 

    for t in returns:
        curr = curr* (1+t)
        result.append(curr-1)

    return result