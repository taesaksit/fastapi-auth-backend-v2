from pydantic import BaseModel, EmailStr


class Register(BaseModel):
    email: EmailStr
    name: str
    password: str


class RegisterOut(BaseModel):
    email: EmailStr
    name: str


class Login(BaseModel):
    email: EmailStr
    password: str


class LoginOut(BaseModel):
    access_token: str
    token_type: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    name: str

    class Config:
        from_attributes = True
