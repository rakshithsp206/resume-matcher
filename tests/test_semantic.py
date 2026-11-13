
import numpy as np

from app.models import semantic_model


def test_get_embeddings(monkeypatch):
    def mock_encode(text):
        return np.array([0.1, 0.2, 0.3])

    monkeypatch.setattr(
        semantic_model.model,
        "encode",
        mock_encode
    )

    documents = [
        "Python developer resume",
        "Python backend developer job"
    ]

    result = semantic_model.get_embeddings(documents)

    assert len(result) == 2
    assert len(result[0]) == 1
    assert len(result[1]) == 1

    assert np.array_equal(
        result[0][0],
        np.array([0.1, 0.2, 0.3])
    )
