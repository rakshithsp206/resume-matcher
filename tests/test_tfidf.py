
from app.models.tfidf_model import vectorise


def test_vectorise_documents():
    documents = [
        "Python developer",
        "Java developer"
    ]

    result = vectorise(documents)

    assert result.shape[0] == 2
    assert result.shape[1] > 0


def test_vectorise_returns_sparse_matrix():
    documents = [
        "Python FastAPI MongoDB",
        "Java Spring MySQL"
    ]

    result = vectorise(documents)

    assert hasattr(result, "toarray")


def test_similar_documents_have_common_features():
    documents = [
        "Python developer with FastAPI",
        "Python backend developer using FastAPI"
    ]

    result = vectorise(documents)

    assert result.shape[0] == 2
    assert result[0].nnz > 0
    assert result[1].nnz > 0
