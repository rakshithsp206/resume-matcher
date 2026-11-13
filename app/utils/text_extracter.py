
import pymupdf

def extract_text_from_pdf(pdf_bytes: bytes) -> str:

    try:
        doc = pymupdf.open(
            stream=pdf_bytes,
            filetype="pdf"
        )

        if doc.is_encrypted:
            raise ValueError(
                "Password-protected PDFs are not supported."
            )

        if len(doc) == 0:
            raise ValueError("The PDF document is empty.")

        extracted_text = []

        for page in doc:
            extracted_text.append(page.get_text())

        doc.close()

        text = "\n".join(extracted_text).strip()

        if not text:
            raise ValueError(
                "No extractable text found in the PDF."
            )

        return text

    except ValueError:
        raise

    except Exception:
        raise ValueError(
            "Unable to process the PDF. It may be corrupted."
        )
