from sklearn.metrics.pairwise import cosine_similarity
    
def calculate_similarity(tfidf_matrix):
    similarity_matrix = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
    return similarity_matrix[0][0]