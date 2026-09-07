def catalog_coverage(recommendations: list, n_items: int) -> float:
    if n_items == 0:
        return 0.0
        
    unique_recommended_items = {
        item 
        for user_recs in recommendations 
        for item in user_recs
    }
    
    return len(unique_recommended_items) / n_items