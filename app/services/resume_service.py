from app.models.tfidf_model import vectorise
from app.utils.text_extracter import extract_text_from_pdf
from app.models.similarity_model import calculate_similarity
from app.utils.text_preprocessor import preprocess_text
from app.models.semantic_model import get_embeddings

def get_similarity_score(resume_text: str, job_desc: str) -> float:
    # Preprocess the extracted resume text and job description
    resume_text = preprocess_text(resume_text)
    job_desc = preprocess_text(job_desc)

    # Combine the resume text and job description into a list
    documents = [resume_text, job_desc]

    # Vectorize the documents using TF-IDF
    embeddings = get_embeddings(documents)

    # Calculate the similarity score using cosine similarity
    similarity_score = calculate_similarity(embeddings)

    return round(similarity_score*100, 2)