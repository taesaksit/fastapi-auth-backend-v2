from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from repository import auth as auth_repo

from schemas import user as schemasUser
from schemas.response import ResponseSchema

router = APIRouter(prefix="/auth")


@router.post("/register", response_model=ResponseSchema[schemasUser.RegisterOut])
def register(user: schemasUser.Register, db: Session = Depends(get_db)):
    return auth_repo.register(db, user)


@router.post("/login", response_model=ResponseSchema[schemasUser.LoginOut])
def login(user: schemasUser.Login, db: Session = Depends(get_db)):
    return auth_repo.login(db, user)

