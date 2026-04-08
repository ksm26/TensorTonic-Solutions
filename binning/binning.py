def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    w = (max(values) - min(values))/num_bins
    if w == 0 :
        return [0]*len(values)

    bins = []
    minimum = min(values)
    for i in range(len(values)):
         
         bins.append(int(min( (values[i]-minimum)/w, num_bins -1) ) )

    return bins