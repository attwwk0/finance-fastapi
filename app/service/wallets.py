
from fastapi import HTTPException
from requests import Session
from app.database import SessionLocal
from app.schemas import CreateWalletRequest
from app.repo import wallets as wallet_repo

def get_balance(db: Session, wallet_name: str | None = None):
    if wallet_name is None:
        wallets = wallet_repo.get_wallets(db)
        return {"total_balance": sum([w.amount for w in wallets])}
    if not wallet_repo.is_wallet_exist(db, wallet_name):
        raise HTTPException(
            status_code=404,
            detail=f"Wallet '{wallet_name}' not found"
        )
    wallet = wallet_repo.get_wallet_balance(db, wallet_name)
    return {"wallet": wallet_name, "balance": wallet.balance}
    

def create_wallet(db: Session, wallet: CreateWalletRequest):
    if wallet_repo.is_wallet_exist(db, wallet.name):
            raise HTTPException(
                status_code=400,
                detail=f"Wallet '{wallet.name}' already exists"
            )
    wallet = wallet_repo.create_wallet(db, wallet.name, wallet.initial_balance)
    db.commit()
    return {
        "message": f"Wallet {wallet.name} created",
        "wallet": wallet.name,
        "balance": wallet.balance
    }