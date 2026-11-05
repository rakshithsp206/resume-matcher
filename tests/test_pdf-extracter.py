
import pymupdf
from pathlib import Path

file_path = Path(__file__).parent / "sample_resume1.pdf"

def extract_text_from_pdf(file_path):
    doc = pymupdf.open(file_path)

    extracted_text = ""

    for page in doc:
        extracted_text += page.get_text() + "\n"

    doc.close()

    return extracted_text


text = extract_text_from_pdf(file_path)

print("Extracted Resume Text:")
print("----------------------")
print(text)
