from app.services.analysis_service import (save_analysis_result, retrieve_analysis_results, retrieve_analysis_result_by_id, remove_analysis_result)
from fastapi import HTTPException, status
from app.schemas.analysis_schema import AnalysisSchema,AnalysisListResponse

def save_analysis_controller(user, analysis_result: dict)-> dict:
    try:
        analysis_id = save_analysis_result(user, analysis_result)
        return {
            "analysis_id": analysis_id,
            "message": "Analysis result saved successfully"
        }
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

def get_analysis_results_controller(user,page:int=1,limit:int=10)->AnalysisListResponse:
    try:
        results = retrieve_analysis_results(user,page,limit)
        return AnalysisListResponse(**results)
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
        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Analysis result not found."
            )
        return {"message": "Analysis result deleted successfully"}
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )