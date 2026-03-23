def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    top_k = recommended[:k]
    top_k_set = set(top_k)
    count = 0 
    for i in relevant:
        if i in top_k_set:
            count += 1 

    precision = count / k 
    recall = count / len(relevant)
    return [precision, recall]