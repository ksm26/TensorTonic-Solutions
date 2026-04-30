def hit_rate_at_k(recommendations, ground_truth, k):
    """
    Compute the hit rate at K.
    """
    count = 0 
    for i in range(len(recommendations)):
        top_k = recommendations[i][:k]
        gt_items = ground_truth[i]
        
        if any(item in top_k for item in gt_items):
            count += 1
            
    return count/len(recommendations)