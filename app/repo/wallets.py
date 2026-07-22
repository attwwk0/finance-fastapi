from decimal import Decimal
from app.database import SessionLocal
from app.models import Wallet
from sqlalchemy.orm import Session



def is_wallet_exist(db: Session, wallet_name:str)-> bool:
    return db.query(Wallet).filter(Wallet.name == wallet_name).first() 


def income_log(db: Session,wallet_name:str, amount:Decimal) ->Wallet:
    wallet = db.query(Wallet).filter(Wallet.name == wallet_name).first() 
    wallet.balance += amount
    return wallet


def get_wallet_balance(db: Session,wallet_name:str)->Wallet:
    return db.query(Wallet).filter(Wallet.name == wallet_name).first() 


def expence_log(db: Session,wallet_name:str, amount:Decimal)->float:
    wallet = db.query(Wallet).filter(Wallet.name == wallet_name).first() 
    wallet.balance -= amount
    return wallet


def get_wallets(db: Session)->list:
    return db.query(Wallet).all()


def create_wallet(db: Session,wallet_name: str, amount: float)->Wallet:

    wallet = Wallet(name = wallet_name, balance = amount)
    db.add(wallet)
    db.flush()
    return wallet