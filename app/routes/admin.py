from fastapi import APIRouter

router = APIRouter()

@router.get("/deposits")
async def list_pending_deposits():
    # Query db for deposits with status == "pending"
    return {"ok": True, "data": [], "message": "List pending deposits - implement DB query"}
