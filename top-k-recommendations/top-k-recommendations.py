def top_k_recommendations(scores, rated_indices, k):
    """
    Return indices of top-k unrated items by predicted score.
    """
    hashmap = {}
    for i in range(len(scores)):
        if i not in rated_indices:
            hashmap[i] = scores[i]
            
    data = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
    
    result = []
    for  key,_ in data:
        if len(result) < k :
            result.append(key)
        else : 
            break

    return result

    