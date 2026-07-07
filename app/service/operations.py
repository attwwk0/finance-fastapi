from fastapi import HTTPException
from app.schemas import OperationRequest
from app.repo import wallets as wallet_repo

def income_log(operation: OperationRequest):
    if not wallet_repo.is_wallet_exist(operation.wallet_name):
        raise HTTPException(
            status_code=404,
            detail=f"Wallet:'{operation.wallet_name}' was not found"
        )
    new_balance = wallet_repo.income_log(operation.wallet_name, operation.amount)

    return {
        "message": "income added",
        "wallet": operation.wallet_name,
        "amount": f"+{operation.amount}",
        "description": operation.description,
        "new_balance": new_balance
    }

def expense_log(operation: OperationRequest):
    if not wallet_repo.is_wallet_exist(operation.wallet_name):
        raise HTTPException(
            status_code=404,
            detail=f"Wallet:'{operation.wallet_name}' was not found"
        )
    balance = wallet_repo.get_wallet_balance(operation.wallet_name)
    if operation.amount > balance:
        raise HTTPException(
            status_code=400,
            detail=f"Insufficient balance! Available: {balance}"
        )
    
    new_expense = wallet_repo.expence_log(operation.wallet_name, operation.amount)

    return {
        "message": "expense added",
        "wallet": operation.wallet_name,
        "amount": f"-{operation.amount}",
        "description": operation.description,
        "new_balance": new_expense
    }