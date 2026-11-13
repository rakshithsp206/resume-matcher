
from unittest.mock import AsyncMock, patch

from bson import ObjectId

from app.schemas.response import ResumeMatchResponse
from app.services.token_service import create_access_token


def get_auth_headers(user_id):
    token = create_access_token({"sub": str(user_id)})
    return {"Authorization": f"Bearer {token}"}


def sample_job_description():
    return {
        "job_title": "Python Developer",
        "company_name": "Google",
        "job_description": (
            "We are looking for a Python developer with "
            "experience in FastAPI, MongoDB, REST APIs and SQL."
        )
    }


def sample_resume_response():
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


def test_resume_analysis_success(client):
    user_id = ObjectId()
    headers = get_auth_headers(user_id)

    pdf_content = b"%PDF-1.4 fake pdf content"

    expected_response = sample_resume_response()

    with (
        patch(
            "app.dependencies.auth_dependency.get_user_by_id",
            return_value={"_id": user_id}
        ),
        patch(
            "app.routes.resume_match.match_resume",
            new_callable=AsyncMock,
            return_value=ResumeMatchResponse(**expected_response)
        ) as mock_match
    ):
        response = client.post(
            "/api/resume",
            headers=headers,
            files={
                "file": (
                    "resume.pdf",
                    pdf_content,
                    "application/pdf"
                )
            },
            data=sample_job_description()
        )

    assert response.status_code == 200

    data = response.json()

    assert data["job_title"] == "Python Developer"
    assert data["company_name"] == "Google"
    assert data["overall_match_percentage"] == 80.0

    mock_match.assert_awaited_once()


def test_resume_analysis_without_token(client):
    response = client.post(
        "/api/resume",
        files={
            "file": (
                "resume.pdf",
                b"fake pdf",
                "application/pdf"
            )
        },
        data=sample_job_description()
    )

    assert response.status_code == 401


def test_resume_analysis_invalid_job_title(client):
    user_id = ObjectId()
    headers = get_auth_headers(user_id)

    with patch(
        "app.dependencies.auth_dependency.get_user_by_id",
        return_value={"_id": user_id}
    ):
        response = client.post(
            "/api/resume",
            headers=headers,
            files={
                "file": (
                    "resume.pdf",
                    b"fake pdf",
                    "application/pdf"
                )
            },
            data={
                **sample_job_description(),
                "job_title": "AI"
            }
        )

    assert response.status_code == 422


def test_resume_analysis_invalid_company_name(client):
    user_id = ObjectId()
    headers = get_auth_headers(user_id)

    with patch(
        "app.dependencies.auth_dependency.get_user_by_id",
        return_value={"_id": user_id}
    ):
        response = client.post(
            "/api/resume",
            headers=headers,
            files={
                "file": (
                    "resume.pdf",
                    b"fake pdf",
                    "application/pdf"
                )
            },
            data={
                **sample_job_description(),
                "company_name": "A"
            }
        )

    assert response.status_code == 422


def test_resume_analysis_invalid_job_description(client):
    user_id = ObjectId()
    headers = get_auth_headers(user_id)

    with patch(
        "app.dependencies.auth_dependency.get_user_by_id",
        return_value={"_id": user_id}
    ):
        response = client.post(
            "/api/resume",
            headers=headers,
            files={
                "file": (
                    "resume.pdf",
                    b"fake pdf",
                    "application/pdf"
                )
            },
            data={
                **sample_job_description(),
                "job_description": "Too short"
            }
        )

    assert response.status_code == 422
