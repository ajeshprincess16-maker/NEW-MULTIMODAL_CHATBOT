from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Dict, Optional
from services.llm_service import llm_service

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    history: List[Dict[str, str]] = []  # format: [{"role": "user", "content": "hi"}, ...]
    conversation_id: Optional[str] = None
    mode: str = "general" # general, document, search, supportive

@router.post("/chat")
async def chat(request: ChatRequest):
    if not request.message.strip():
        return {"response": "Message cannot be empty.", "mode": request.mode}
        
    response_text = llm_service.generate_response(
        prompt=request.message,
        history=request.history
    )
    return {"response": response_text, "mode": request.mode}

@router.get("/conversations")
async def get_conversations():
    return []

@router.get("/conversations/{id}")
async def get_conversation(id: str):
    return {"id": id, "messages": []}

@router.delete("/conversations/{id}")
async def delete_conversation(id: str):
    return {"status": "deleted"}
