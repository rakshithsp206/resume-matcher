
from types import SimpleNamespace

import pymupdf
import pytest

from app.utils.pdf_validator import validate_pdf_file


def create_pdf_bytes(page_count=1):
    """Generate a PDF in memory."""
    doc = pymupdf.open()

    for _ in range(page_count):
        doc.new_page()

    pdf_bytes = doc.tobytes()
    doc.close()

    return pdf_bytes


def create_upload_file(
    filename="resume.pdf",
    content_type="application/pdf"
):
    return SimpleNamespace(
        filename=filename,
        content_type=content_type
    )


def test_valid_pdf():
    file = create_upload_file()
    pdf_bytes = create_pdf_bytes()

    validate_pdf_file(file, pdf_bytes)


def test_invalid_extension():
    file = create_upload_file(filename="resume.txt")
    pdf_bytes = create_pdf_bytes()

    with pytest.raises(ValueError, match="Only PDF files"):
        validate_pdf_file(file, pdf_bytes)


def test_invalid_content_type():
    file = create_upload_file(content_type="text/plain")
    pdf_bytes = create_pdf_bytes()

    with pytest.raises(ValueError, match="Invalid file type"):
        validate_pdf_file(file, pdf_bytes)


def test_file_size_exceeds_limit():
    file = create_upload_file()

    # Create data larger than the configured file size limit.
    pdf_bytes = b"%PDF-" + b"x" * (5 * 1024 * 1024)

    with pytest.raises(ValueError, match="5 MB"):
        validate_pdf_file(file, pdf_bytes)


def test_invalid_pdf_signature():
    file = create_upload_file()
    pdf_bytes = b"This is not a PDF"

    with pytest.raises(ValueError, match="Invalid PDF"):
        validate_pdf_file(file, pdf_bytes)


def test_pdf_exceeds_page_limit():
    file = create_upload_file()
    pdf_bytes = create_pdf_bytes(page_count=16)

    with pytest.raises(ValueError, match="15 pages"):
        validate_pdf_file(file, pdf_bytes)
