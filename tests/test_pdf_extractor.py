
import pymupdf
import pytest

from app.utils.text_extracter import extract_text_from_pdf


@pytest.fixture
def sample_pdf_bytes():
    """Create a PDF containing sample text in memory."""
    doc = pymupdf.open()

    page = doc.new_page()
    page.insert_text((72, 72), "Hello, this is a test resume.")

    pdf_bytes = doc.tobytes()
    doc.close()

    return pdf_bytes


@pytest.fixture
def empty_pdf_bytes():
    """Create a valid PDF with one blank page."""
    doc = pymupdf.open()
    doc.new_page()

    pdf_bytes = doc.tobytes()
    doc.close()

    return pdf_bytes


def test_extract_text_from_valid_pdf(sample_pdf_bytes):
    extracted_text = extract_text_from_pdf(sample_pdf_bytes)

    assert isinstance(extracted_text, str)
    assert "Hello, this is a test resume." in extracted_text


def test_extract_text_from_empty_pdf(empty_pdf_bytes):
    with pytest.raises(ValueError):
        extract_text_from_pdf(empty_pdf_bytes)


def test_extract_text_from_invalid_pdf():
    invalid_pdf = b"This is not a PDF file"

    with pytest.raises(ValueError):
        extract_text_from_pdf(invalid_pdf)
