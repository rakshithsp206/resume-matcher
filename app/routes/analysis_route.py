from fastapi import APIRouter, Depends
from app.dependencies.auth_dependency import get_current_user
from app.controllers.analysis_controller import (save_analysis_controller,
                                                get_analysis_results_controller,    
                                            get_analysis_result_by_id_controller,
                                            delete_analysis_result_controller)
from app.schemas.analysis_schema import AnalysisSchema
from app.schemas.response import ResumeMatchResponse

router = APIRouter()

@router.post("/", response_model=str)
def save_analysis_result(analysis_result: ResumeMatchResponse, user: dict = Depends(get_current_user)):
    return save_analysis_controller(user, analysis_result.dict())

@router.get("/", response_model=list[AnalysisSchema])
def get_analysis_results(user: dict = Depends(get_current_user)):
    return get_analysis_results_controller(user)

@router.get("/{analysis_id}", response_model=AnalysisSchema)
def get_analysis_result_by_id(analysis_id: str, user: dict = Depends(get_current_user)):
    return get_analysis_result_by_id_controller(analysis_id, user)

@router.delete("/{analysis_id}", response_model=dict)
def delete_analysis_result(analysis_id: str,user: dict = Depends(get_current_user)):
    return delete_analysis_result_controller(analysis_id, user)