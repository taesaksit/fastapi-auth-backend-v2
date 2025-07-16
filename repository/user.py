from sqlalchemy.orm import Session
from models.user import User


from schemas import user as schemasUser
from schemas.response import ResponseSchema


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_all_users(db: Session):
    users = db.query(User).all()
    user_out_list = []
    for user in users:
        user_out = schemasUser.UserOut.model_validate(user)
        user_out_list.append(user_out)

    return ResponseSchema(
        status="success", message="List all users", data=user_out_list
    )
