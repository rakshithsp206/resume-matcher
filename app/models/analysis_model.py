from datetime import datetime
from app.database.mongodb import analysis_collection

def insert_analysis_result(user_id: str, analysis_result: dict)-> str:
    analysis_result["user_id"] = str(user_id)
    analysis_result["created_at"] = datetime.utcnow()
    result = analysis_collection.insert_one(analysis_result)
    return str(result.inserted_id)

def get_analysis_results_by_user(user_id: str)-> list[dict]:
    return list(analysis_collection.find({"user_id": str(user_id)}))

def get_analysis_result_by_id(analysis_id: str, user_id: str)-> dict:
    from bson import ObjectId
    from bson.errors import InvalidId

    try:
        result = analysis_collection.find_one({"_id": ObjectId(analysis_id), "user_id": str(user_id)})
        if not result:
            raise ValueError("Analysis result not found.")
        return result
    except InvalidId:
        raise ValueError("Invalid analysis ID format.")

def delete_analysis_result(analysis_id: str, user_id: str)-> bool:
    from bson import ObjectId
    from bson.errors import InvalidId

    try:
        result = analysis_collection.delete_one({"_id": ObjectId(analysis_id), "user_id": str(user_id)})
        if result.deleted_count == 0:
            raise ValueError("Analysis result not found.")
        return True
    except InvalidId:
        raise ValueError("Invalid analysis ID format.")