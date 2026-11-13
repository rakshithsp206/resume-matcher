from datetime import datetime,timezone
from app.database.mongodb import analysis_collection

analysis_collection.create_index(
    [("user_id", 1), ("created_at", -1)]
)

def insert_analysis_result(user_id: str, analysis_result: dict)-> str:
    analysis_result["user_id"] = str(user_id)
    analysis_result["created_at"] = datetime.now(timezone.utc)  
    result = analysis_collection.insert_one(analysis_result)
    return str(result.inserted_id)

def get_analysis_results_by_user(user_id: str,page:int=1,limit:int=10)-> list[dict]:
    skip=(page-1)*limit
    return list(analysis_collection.find({"user_id": str(user_id)}).sort("created_at", -1).skip(skip).limit(limit))

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
            return False
        return True
    except InvalidId:
        raise ValueError("Invalid analysis ID format.")

def count_user_analyses(user_id: str) -> int:
    return analysis_collection.count_documents({
        "user_id": str(user_id)
    })