def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    dict = {}
    
    for arr in sentences:
        for arr2 in arr :
            if arr2 in dict.keys():
                dict[arr2] += 1 
            else : 
                dict[arr2] = 1
    return dict