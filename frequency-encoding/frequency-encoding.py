from collections import Counter
def frequency_encoding(values):
    """
    Replace each value with its frequency proportion.
    """
    listt = Counter(values)
    result = []
    for i in values:
        result.append(listt[i]/len(values))

    return result