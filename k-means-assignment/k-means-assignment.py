def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    assignments = []
    
    for p in points:
        best_dist = float('inf') 
        best_idx = 0 
        for i, c in enumerate(centroids):
            dist = 0 
            for d in range(len(p)):
                dist += (p[d] - c[d]) ** 2
             # Update nearest centroid
            if dist < best_dist:
                best_dist = dist
                best_idx = i
        
        assignments.append(best_idx)

    return assignments

        