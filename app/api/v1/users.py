from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from app.dependancy import get_db

from app.schemas import UserReq, UserRes

from app.service import users as users_service 
router=FastAPI()

@router.post("/users", response_model=UserRes)

def create_user(payload: UserReq, db: Session = Depends(get_db)):
    return users_service.create_user(payload)

