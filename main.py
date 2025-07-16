from fastapi import FastAPI, HTTPException
from database import Base, engine
from utils import exception_handlers
from routes import auth, user

app = FastAPI()

Base.metadata.create_all(bind=engine)
app.add_exception_handler(HTTPException,exception_handlers.http_exception_handler)

app.include_router(auth.router, prefix="/api")
app.include_router(user.router, prefix="/api")


@app.get("/")
def root():
    return {"message":"FastAPI-Authentication !!!"}