from app.models.analysis_model import (get_analysis_results_by_user, 
                                        get_analysis_result_by_id, 
                                        delete_analysis_result, 
                                        insert_analysis_result,
                                        count_user_analyses)

def save_analysis_result(user: dict, analysis_result: dict)-> str:
    user_id = user.get("_id")
    if not user_id:
        raise ValueError("User ID is missing.")
    
    analysis_id = insert_analysis_result(user_id, analysis_result)
    return analysis_id

def retrieve_analysis_results(user: dict,page:int=1,limit:int=10)-> list[dict]:
    user_id = user.get("_id")
    if not user_id:
        raise ValueError("User ID is missing.")
    
    analyses = get_analysis_results_by_user(user_id,page,limit)

    total = count_user_analyses(user_id)

    total_pages = (total + limit - 1) // limit
    return {
        "page": page,
        "limit": limit,
        "total": total,
        "total_pages": total_pages,
        "analyses": analyses
    }

def retrieve_analysis_result_by_id(analysis_id: str, user: dict)-> dict:
    user_id = user.get("_id")
    if not user_id:
        raise ValueError("User ID is missing.")

    result = get_analysis_result_by_id(analysis_id, user_id)
    return result

def remove_analysis_result(analysis_id: str, user: dict)-> dict:
    user_id = user.get("_id")
    if not user_id:
        raise ValueError("User ID is missing.")

    success = delete_analysis_result(analysis_id, user_id)
    return success