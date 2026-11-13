
import pymupdf


MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB
MAX_PAGES = 15


def validate_pdf_file(file, file_bytes: bytes):

    # 1. Check file extension
    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise ValueError("Only PDF files are allowed.")

    # 2. Check MIME type
    if file.content_type != "application/pdf":
        raise ValueError("Invalid file type. Please upload a PDF.")

    # 3. Check file size
    if len(file_bytes) > MAX_FILE_SIZE:
        raise ValueError("File size cannot exceed 5 MB.")

    # 4. Check PDF signature
    if not file_bytes.startswith(b"%PDF-"):
        raise ValueError("Invalid PDF file.")

    # 5. Check PDF integrity and page count
    try:
        doc = pymupdf.open(stream=file_bytes, filetype="pdf")

        if doc.is_encrypted:
            doc.close()
            raise ValueError("Password-protected PDFs are not supported.")

        if len(doc) == 0:
            doc.close()
            raise ValueError("The PDF document is empty.")

        if len(doc) > MAX_PAGES:
            doc.close()
            raise ValueError(
                f"PDF cannot contain more than {MAX_PAGES} pages."
            )

        doc.close()

    except ValueError:
        raise

    except Exception:
        raise ValueError("Invalid or corrupted PDF file.")
