from app.schemas import OperationRequest
from fastapi import APIRouter
from app.service import operations as wallets_operations

router = APIRouter()

@router.post("/operations/income")
def income_log(operation: OperationRequest):
    return wallets_operations.income_log(operation)


@router.post("/operations/expense")
def expense_log(operation: OperationRequest):
    return wallets_operations.expense_log(operation)