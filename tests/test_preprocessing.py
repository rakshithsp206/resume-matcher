
import re
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize

# Download stopwords
nltk.download("stopwords")

stop_words = set(stopwords.words("english"))

def preprocess_text(text: str) -> str:

    # 1. Convert to lowercase
    text = text.lower()

    # 2. Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # 3. Remove email addresses
    text = re.sub(r"\S+@\S+", "", text)

    # 4. Remove special characters
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)

    # 5. Tokenization
    tokens = wordpunct_tokenize(text)

    # 6. Remove stopwords
    tokens = [
        word for word in tokens
        if word not in stop_words
    ]

    return " ".join(tokens)


sample_text = """
Experienced Python Developer with 2+ years of experience.
Skilled in Python, Machine Learning, SQL, and Data Analysis.
"""

cleaned_text = preprocess_text(sample_text)

print("Original Text:")
print(sample_text)

print("\nPreprocessed Text:")
print(cleaned_text)
