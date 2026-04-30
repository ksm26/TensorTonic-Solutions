def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    result = []
    for item in items :
        avgrating, numvotes = item[0], item[1]
        value = (numvotes/(numvotes+min_votes))*avgrating + (min_votes/(numvotes+min_votes))*global_mean

        result.append(value)

    return result 