from app.schemas import OperationRequest
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependancy import get_db
from app.service import operations as wallets_operations

router = APIRouter()

@router.post("/operations/income")
def income_log(operation: OperationRequest,db: Session = Depends(get_db)):
    return wallets_operations.income_log(db, operation)


@router.post("/operations/expense")
def expense_log(operation: OperationRequest,db: Session = Depends(get_db)):
    return wallets_operations.expense_log(db,operation)