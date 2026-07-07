
from fastapi import HTTPException
from app.schemas import CreateWalletRequest
from app.repo import wallets as wallet_repo

def get_balance(wallet_name: str | None = None):
    if wallet_name is None:
        wallets = wallet_repo.get_wallets()
        return {"total_balance": sum(wallets.values())}
    if not wallet_repo.is_wallet_exist(wallet_name):
        raise HTTPException(
            status_code=404,
            detail=f"Wallet '{wallet_name}' not found"
        )
    return {"wallet": wallet_name, "balance": wallet_repo.get_wallet_balance(wallet_name)}

def create_wallet(wallet: CreateWalletRequest):
    if wallet_repo.is_wallet_exist(wallet.name):
            raise HTTPException(
                status_code=400,
                detail=f"Wallet '{wallet.name}' already exists"
            )
    balance = wallet_repo.create_wallet(wallet.name, wallet.initial_balance)
    
    return {
        "message": f"Wallet {wallet.name} created",
        "wallet": wallet.name,
        "balance": balance
    }