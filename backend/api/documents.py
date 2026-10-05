from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/documents")
async def upload_document(file: UploadFile = File(...)):
    return {"filename": file.filename, "status": "uploaded"}

@router.get("/documents")
async def get_documents():
    return []

@router.get("/documents/{id}")
async def get_document(id: str):
    return {"id": id, "filename": "example.pdf"}

@router.put("/documents/{id}")
async def update_document(id: str, file: UploadFile = File(...)):
    return {"id": id, "status": "updated"}

@router.delete("/documents/{id}")
async def delete_document(id: str):
    return {"status": "deleted"}
