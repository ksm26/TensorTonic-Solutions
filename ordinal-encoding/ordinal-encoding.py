def ordinal_encoding(values, ordering):
    """
    Encode categorical values using the provided ordering.
    """
    data = {}
    for i in range(len(ordering)) :
        if ordering[i] not in data :
            data[ordering[i]] = i

    res = []
    for i in range(len(values)):
        res.append(data[values[i]])

    return res