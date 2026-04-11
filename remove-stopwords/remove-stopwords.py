def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    stopwords = set(stopwords)
    res = []
    for i in tokens:
        if i not in stopwords:
            res.append(i)
    return res
    