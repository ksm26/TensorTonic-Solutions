from collections import defaultdict
import numpy as np 
def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    data = defaultdict(list)
    for i in range(len(categories)):
        data[categories[i]].append(targets[i])

    rawdict = {}
    for key,value in data.items() :
        rawdict[key] = np.mean(value)

    res = []
    for i in  categories:
        res.append(rawdict[i])

    return res