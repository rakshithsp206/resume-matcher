def match_percentage(semantic_similarity_percentage: float, skill_match_percentage: float) -> float:
    return round((6*semantic_similarity_percentage + 4*skill_match_percentage) / 10, 2)