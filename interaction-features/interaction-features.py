def interaction_features(X):
    """
    Generate pairwise interaction features and append them to the original features.
    """
    # Write code here
    result = []
    
    for row in X:
        new_row = row[:]

        for i in range(len(row)):
            for j in range(i+1, len(row)):
                new_row.append(row[i] * row[j])
    
        result.append(new_row)

    return result