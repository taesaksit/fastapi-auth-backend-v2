from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from core.security import hash_password, verify_password, create_access_token
from models.user import User as UserModel
from repository.user import get_user_by_email


from schemas import user as schemasUser
from schemas.response import ResponseSchema


# Register
def register(db: Session, user: schemasUser.Register):
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Email already exists"
        )

    new_user = UserModel(
        email=user.email, name=user.name, password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return ResponseSchema(
        status="success", message="Register successfully", data=new_user
    )


# Login
def login(db: Session, user: schemasUser.Login):
    db_user = get_user_by_email(db, user.email)
    if not db_user or not verify_password(user.password, db_user.password):

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="email or password incorrect",
        )

    user_response = {"sub": db_user.email, "id": db_user.id, "name": db_user.name}

    token = create_access_token(data={**user_response})
    return ResponseSchema(
        status="success",
        message="Login successfully",
        data={"access_token": token, "token_type": "Bearer"},
    )
