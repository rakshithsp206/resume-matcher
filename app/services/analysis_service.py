from app.models.analysis_model import (get_analysis_results_by_user, 
                                        get_analysis_result_by_id, 
                                        delete_analysis_result, 
                                        insert_analysis_result)

def save_analysis_result(user: dict, analysis_result: dict)-> str:
    user_id = user.get("_id")
    if not user_id:
        raise ValueError("User ID is missing.")
    
    analysis_id = insert_analysis_result(user_id, analysis_result)
    return analysis_id

def retrieve_analysis_results(user: dict)-> list[dict]:
    user_id = user.get("_id")
    if not user_id:
        raise ValueError("User ID is missing.")
    
    results = get_analysis_results_by_user(user_id)
    return results

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