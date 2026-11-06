from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embeddings(documents):
    resume_embedding = model.encode(documents[0])
    job_desc_embedding = model.encode(documents[1])
    return [[resume_embedding], [job_desc_embedding]]