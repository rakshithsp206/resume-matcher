
from datetime import datetime, timezone
from unittest.mock import patch

from bson import ObjectId
from app.services.token_service import create_access_token


def get_auth_headers(user_id):
    token = create_access_token({"sub": str(user_id)})
    return {"Authorization": f"Bearer {token}"}


def sample_analysis():
    return {
        "job_title": "Python Developer",
        "company_name": "Google",
        "semantic_match_percentage": 85.5,
        "skills": {
            "matched_skills": ["Python", "FastAPI"],
            "missing_skills": ["Docker"],
            "additional_skills": ["Java"],
            "skill_match_percentage": 75.0
        },
        "projects": [],
        "overall_match_percentage": 80.0
    }


def sample_saved_analysis(user_id, analysis_id):
    return {
        **sample_analysis(),
        "_id": analysis_id,
        "user_id": str(user_id),
        "created_at": datetime.now(timezone.utc)
    }


def test_save_analysis(client):
    user_id = ObjectId()
    analysis_id = str(ObjectId())
    headers = get_auth_headers(user_id)

    with (
        patch(
            "app.dependencies.auth_dependency.get_user_by_id",
            return_value={"_id": user_id}
        ),
        patch(
            "app.controllers.analysis_controller.save_analysis_result",
            return_value=analysis_id
        )
    ):
        response = client.post(
            "/api/analysis/",
            json=sample_analysis(),
            headers=headers
        )

    assert response.status_code == 201



def test_get_all_analyses(client):
    user_id = ObjectId()
    analysis_id = ObjectId()
    headers = get_auth_headers(user_id)

    saved_analysis = sample_saved_analysis(user_id, analysis_id)

    mock_results = {
        "page": 1,
        "limit": 10,
        "total": 1,
        "total_pages": 1,
        "analyses": [saved_analysis]
    }

    with (
        patch(
            "app.dependencies.auth_dependency.get_user_by_id",
            return_value={"_id": user_id}
        ),
        patch(
            "app.controllers.analysis_controller.retrieve_analysis_results",
            return_value=mock_results
        )
    ):
        response = client.get(
            "/api/analysis/",
            headers=headers
        )

    assert response.status_code == 200

    data = response.json()

    assert data["page"] == 1
    assert data["limit"] == 10
    assert data["total"] == 1
    assert data["total_pages"] == 1
    assert len(data["analyses"]) == 1
    assert data["analyses"][0]["user_id"] == str(user_id)



def test_get_single_analysis(client):
    user_id = ObjectId()
    analysis_id = ObjectId()
    headers = get_auth_headers(user_id)

    saved_analysis = sample_saved_analysis(user_id, analysis_id)

    with (
        patch(
            "app.dependencies.auth_dependency.get_user_by_id",
            return_value={"_id": user_id}
        ),
        patch(
            "app.controllers.analysis_controller.retrieve_analysis_result_by_id",
            return_value=saved_analysis
        )
    ):
        response = client.get(
            f"/api/analysis/{analysis_id}",
            headers=headers
        )

    assert response.status_code == 200


def test_get_nonexistent_analysis(client):
    user_id = ObjectId()
    analysis_id = ObjectId()
    headers = get_auth_headers(user_id)

    with (
        patch(
            "app.dependencies.auth_dependency.get_user_by_id",
            return_value={"_id": user_id}
        ),
        patch(
            "app.controllers.analysis_controller.retrieve_analysis_result_by_id",
            side_effect=ValueError("Analysis not found")
        )
    ):
        response = client.get(
            f"/api/analysis/{analysis_id}",
            headers=headers
        )

    assert response.status_code == 404


def test_user_cannot_access_other_users_analysis(client):
    user_id = ObjectId()
    analysis_id = ObjectId()
    headers = get_auth_headers(user_id)

    with (
        patch(
            "app.dependencies.auth_dependency.get_user_by_id",
            return_value={"_id": user_id}
        ),
        patch(
            "app.controllers.analysis_controller.retrieve_analysis_result_by_id",
            side_effect=ValueError("Analysis not found")
        )
    ):
        response = client.get(
            f"/api/analysis/{analysis_id}",
            headers=headers
        )

    assert response.status_code == 404


def test_delete_analysis(client):
    user_id = ObjectId()
    analysis_id = ObjectId()
    headers = get_auth_headers(user_id)

    with (
        patch(
            "app.dependencies.auth_dependency.get_user_by_id",
            return_value={"_id": user_id}
        ),
        patch(
            "app.controllers.analysis_controller.remove_analysis_result",
            return_value=True
        )
    ):
        response = client.delete(
            f"/api/analysis/{analysis_id}",
            headers=headers
        )

    assert response.status_code == 200


def test_delete_nonexistent_analysis(client):
    user_id = ObjectId()
    analysis_id = ObjectId()
    headers = get_auth_headers(user_id)

    with (
        patch(
            "app.dependencies.auth_dependency.get_user_by_id",
            return_value={"_id": user_id}
        ),
        patch(
            "app.controllers.analysis_controller.remove_analysis_result",
            side_effect=ValueError("Analysis not found")
        )
    ):
        response = client.delete(
            f"/api/analysis/{analysis_id}",
            headers=headers
        )

    assert response.status_code == 400


def test_analysis_endpoint_without_token(client):
    response = client.get("/api/analysis/")

    assert response.status_code == 401
