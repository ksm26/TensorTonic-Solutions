def min_max_scaling(data):
    rows = len(data)
    cols = len(data[0])
    
    # Step 1: compute min and max for each column
    min_vals = [min(data[i][j] for i in range(rows)) for j in range(cols)]
    max_vals = [max(data[i][j] for i in range(rows)) for j in range(cols)]
    
    # Step 2: scale data
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            r = max_vals[j] - min_vals[j]
            if r == 0:
                row.append(0.0)   # avoid division by zero
            else:
                val = (data[i][j] - min_vals[j]) / r
                row.append(val)
        result.append(row)
    
    return result