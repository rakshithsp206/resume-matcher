import pymupdf

def extract_text_from_pdf(pdf_bytes):
    doc = pymupdf.open(stream=pdf_bytes, filetype="pdf")

    extracted_text = ""

    for page in doc:
        extracted_text += page.get_text() + "\n"

    doc.close()

    return extracted_text