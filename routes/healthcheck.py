from fastapi import APIRouter, status
from datetime import datetime, UTC

router = APIRouter()


@router.get("/healthcheck/", status_code=status.HTTP_200_OK)
async def healthcheck():
    return {
        'status': 'ok',
        'timestamp': datetime.now(UTC)
    }
