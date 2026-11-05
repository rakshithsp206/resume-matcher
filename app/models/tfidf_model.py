from sklearn.feature_extraction.text import TfidfVectorizer

def vectorise(documents):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    return tfidf_matrix