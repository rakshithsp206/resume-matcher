import re
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize

stop_words = set(stopwords.words("english"))

# Preserve important technical terms
def normalize_technical_terms(text: str) -> str:
    replacements = {
        "c++": "cpp",
        "c#": "csharp",
        "node.js": "nodejs"
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text

def preprocess_text(text: str) -> str:

    # 1. Convert to lowercase
    text = text.lower()

    # 2. Normalize technical terms
    text = normalize_technical_terms(text)

    # 3. Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # 4. Remove email addresses
    text = re.sub(r"\S+@\S+", "", text)

    # 5. Remove special characters
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)

    # 6. Tokenization
    tokens = wordpunct_tokenize(text)

    # 7. Remove stopwords
    tokens = [
        word for word in tokens
        if word not in stop_words
    ]

    return " ".join(tokens)