def catalog_coverage(recommendations, n_items):
    """
    Compute the catalog coverage of a recommender system.
    """
    seen = set()
    for row in recommendations:
        for num in row:
            seen.add(num)

    return len(seen)/n_items