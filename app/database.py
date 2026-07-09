from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

BALANCE_URL = "sqlite:///./finance.db"
engine=create_engine(BALANCE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()