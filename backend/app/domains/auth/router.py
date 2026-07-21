from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.domains.auth.schemas import UserCreate, UserResponse
from app.domains.auth.service import create_user


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.post(
    "/register",
    response_model=UserResponse
)
def register(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    try:
        return create_user(db, user_data)

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error)
        )
