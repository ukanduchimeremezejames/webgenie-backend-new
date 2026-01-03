from fastapi import APIRouter, UploadFile
import shutil, os, uuid

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/")
async def upload_file(file: UploadFile):
    filename = f"{UPLOAD_DIR}/{uuid.uuid4()}-{file.filename}"
    with open(filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": filename}
