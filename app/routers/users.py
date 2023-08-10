from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing_extensions import Annotated

from app.schemas.users import UserCreate, User
from app.backend.session import get_db
from app.services.auth import get_current_active_user
from app.services.users import get_user_by_email, create_user

router = APIRouter()

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user


# Create new user
@router.post("/", response_model=User)
def post_user(user: UserCreate, db: Session = Depends(get_db)):
    print(user)
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)
