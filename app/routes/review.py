from fastapi import APIRouter
from pydantic import BaseModel
from app.services.llm_service import review_code
from app.db.mongo import reviews_collection
import json
from datetime import datetime

router = APIRouter()

class CodeRequest(BaseModel):
    code: str
    language: str

@router.post("/review")
async def review(request: CodeRequest):
    result = review_code(request.code, request.language)
    
    try:
        parsed = json.loads(result)
    except:
        parsed = {"raw": result}
    
    # Save to MongoDB
    reviews_collection.insert_one({
        "language": request.language,
        "code": request.code,
        "review": parsed,
        "created_at": datetime.utcnow()
    })
    
    return {"status": "success", "review": parsed}

@router.get("/history")
async def history():
    reviews = list(reviews_collection.find({}, {"_id": 0}).sort("created_at", -1).limit(10))
    return {"reviews": reviews}