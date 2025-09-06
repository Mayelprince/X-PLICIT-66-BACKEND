from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from datetime import datetime
import uuid
from app.services.storage import upload_image
# from app.db import db  # wire db in real app

router = APIRouter()

@router.post("/upload")
async def upload_screenshot(file: UploadFile = File(...)):
    # Basic validation
    if file.content_type not in ("image/png", "image/jpeg", "image/jpg"):
        raise HTTPException(status_code=400, detail="Invalid image type")
    # Upload to Cloudinary (blocking call in this simple scaffold)
    url = upload_image(file.file)
    return {"success": True, "url": url}

@router.post("/")
async def create_deposit(payload: dict):
    """
    payload should include: user_id, amount (int), sender_name (str), screenshot_url (str)
    For now we just create a placeholder response. In real app store in db with status 'pending'
    """
    deposit = {
        "id": str(uuid.uuid4()),
        "user_id": payload.get("user_id"),
        "amount": int(payload.get("amount", 0)),
        "screenshot_url": payload.get("screenshot_url"),
        "status": "pending",
        "created_at": datetime.utcnow().isoformat()
    }
    # store deposit in db.deposits
    return {"ok": True, "deposit": deposit}
