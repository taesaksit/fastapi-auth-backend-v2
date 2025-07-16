from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from core.oauth2 import get_current_user
from models.user import User

from schemas.user import UserOut
from schemas.response import ResponseSchema

from repository import user as user_repo

router = APIRouter(prefix="/user")


@router.get("/", response_model=ResponseSchema[list[UserOut]])
def get_users(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):
    return user_repo.get_all_users(db)
