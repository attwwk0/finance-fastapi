from fastapi import HTTPException
from app.database import SessionLocal
from app.schemas import OperationRequest
from app.repo import wallets as wallet_repo

def income_log(operation: OperationRequest):
    db = SessionLocal()
    try:
        if not wallet_repo.is_wallet_exist(db, operation.wallet_name):
            raise HTTPException(
                status_code=404,
                detail=f"Wallet:'{operation.wallet_name}' was not found"
            )
        wallet = wallet_repo.income_log(db, operation.wallet_name, operation.amount)

        db.commit()
        return {
            "message": "income added",
            "wallet": operation.wallet_name,
            "amount": f"+{operation.amount}",
            "description": operation.description,
            "new_balance": wallet.balance
        }
    finally:
        db.close()

def expense_log(operation: OperationRequest):
    db = SessionLocal()
    try:
        if not wallet_repo.is_wallet_exist(db, operation.wallet_name):
            raise HTTPException(
                status_code=404,
                detail=f"Wallet:'{operation.wallet_name}' was not found"
            )
        wallet = wallet_repo.get_wallet_balance(db, operation.wallet_name)
        if operation.amount > wallet.balance:
            raise HTTPException(
                status_code=400,
                detail=f"Insufficient balance! Available: {wallet.balance}"
            )
        
        wallet = wallet_repo.expence_log(db, operation.wallet_name, operation.amount)

        db.commit()
        return {
            "message": "expense added",
            "wallet": operation.wallet_name,
            "amount": f"-{operation.amount}",
            "description": operation.description,
            "new_balance": wallet.balance

        
        }
    finally:
        db.close()