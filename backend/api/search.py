from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class SearchRequest(BaseModel):
    query: str

@router.post("/search")
async def web_search(request: SearchRequest):
    return {"query": request.query, "results": []}
