def ordinal_encoding(values, ordering):
    """
    Encode categorical values using the provided ordering.
    """
    hash = {}
    for i in range(len(ordering)):
        hash[ordering[i]] = i 

    result = []

    for i in values:
        result.append(hash[i])

    return result 