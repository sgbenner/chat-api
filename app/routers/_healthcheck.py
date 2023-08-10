from datetime import datetime

from fastapi import APIRouter

router = APIRouter(prefix="")


@router.get("/healthcheck")
def root():
    return {"status": "online", "time": datetime.now()}
