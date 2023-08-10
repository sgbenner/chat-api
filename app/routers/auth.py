from datetime import datetime, timedelta

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing_extensions import Annotated

from app.backend.session import get_db
from app.const import (
    AUTH_TAGS,
    AUTH_URL,
    ACCESS_TOKEN_EXPIRE_MINUTES
)
from app.schemas.auth import TokenSchema
from app.services.auth import authenticate_user, create_access_token

router = APIRouter(prefix="/" + AUTH_URL, tags=AUTH_TAGS)

@router.post("/login", response_model=TokenSchema)
async def authenticate(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                       db: Session = Depends(get_db)):
    user = authenticate_user(db=db, email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
