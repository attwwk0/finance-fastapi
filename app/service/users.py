from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models import User
from app.repo import users as users_repo
from app.schemas import UserRes

def create_user(db: Session, login: str):
    if users_repo.get_user(db, login):
        raise HTTPException(status_code = 400, message = "User already exists")
    user = users_repo.create_user(db, login)
    db.commit()
    return UserRes.model_validate(user)