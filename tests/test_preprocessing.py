
import pytest

from app.utils.text_preprocessor import preprocess_text


def test_lowercase_conversion():
    result = preprocess_text("PYTHON DEVELOPER")

    assert result == "python developer"


def test_stopword_removal():
    result = preprocess_text("The developer is working")

    assert result == "developer working"


def test_url_removal():
    result = preprocess_text(
        "Visit https://example.com for more information"
    )

    assert "https" not in result
    assert "example" not in result
    assert "information" in result


def test_email_removal():
    result = preprocess_text(
        "Contact me at test@example.com"
    )

    assert "test" not in result
    assert "example" not in result
    assert "contact" in result


def test_technical_term_normalization():
    result = preprocess_text("C++ C# Node.js")

    assert result == "cpp csharp nodejs"


def test_special_character_removal():
    result = preprocess_text("Python??? Developer!!!")

    assert result == "python developer"


def test_empty_string():
    result = preprocess_text("")

    assert result == ""
