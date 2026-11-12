from app.services.analysis_service import (save_analysis_result, retrieve_analysis_results, retrieve_analysis_result_by_id, remove_analysis_result)
from fastapi import HTTPException, status
from app.schemas.analysis_schema import AnalysisSchema

def save_analysis_controller(user, analysis_result: dict)-> str:
    try:
        analysis_id = save_analysis_result(user, analysis_result)
        return analysis_id
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

def get_analysis_results_controller(user)-> list[AnalysisSchema]:
    try:
        results = retrieve_analysis_results(user)
        return [AnalysisSchema(**result) for result in results]
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

def get_analysis_result_by_id_controller(analysis_id: str, user: dict)-> AnalysisSchema:
    try:
        result = retrieve_analysis_result_by_id(analysis_id, user)
        return AnalysisSchema(**result)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

def delete_analysis_result_controller(analysis_id: str, user: dict)-> dict:
    try:
        success = remove_analysis_result(analysis_id, user)
        return {"message": "Analysis result deleted successfully"}
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )