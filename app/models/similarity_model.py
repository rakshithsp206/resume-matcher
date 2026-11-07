from sklearn.metrics.pairwise import cosine_similarity
    
def calculate_similarity(embeddings: list[list[float]]) -> float:
    similarity_matrix = cosine_similarity(embeddings[0], embeddings[1])
    return float(similarity_matrix[0][0])