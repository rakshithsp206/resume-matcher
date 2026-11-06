from utils.text_extracter import extract_text_from_pdf
from models.tfidf_model import vectorise
from models.similarity_model import calculate_similarity
from utils.text_preprocessor import preprocess_text
from models.semantic_model import get_embeddings

def get_similarity_score(pdf_bytes, job_desc):

    # Extract text from the uploaded resume PDF
    resume_text = extract_text_from_pdf(pdf_bytes)

    # Preprocess the extracted resume text and job description
    resume_text = preprocess_text(resume_text)
    job_desc = preprocess_text(job_desc)

    # Combine the resume text and job description into a list
    documents = [resume_text, job_desc]

    # Vectorize the documents using TF-IDF
    embeddings = get_embeddings(documents)

    # Calculate the similarity score using cosine similarity
    similarity_score = calculate_similarity(embeddings)

    return similarity_score