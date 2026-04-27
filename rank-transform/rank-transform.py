def rank_transform(values):
    """
    Replace each value with its average rank.
    """
    original = values[:]
    sorted_vals = sorted(values)
    hashmap = {}
    result = []

    for i in range(len(sorted_vals)):
        num = sorted_vals[i]
        if num in hashmap : 
            hashmap[num].append(i+1)
        else : 
            hashmap[num] = [i+1]

    for i in values : 
        result.append(sum(hashmap[i])/len(hashmap[i]))
    

    return result 