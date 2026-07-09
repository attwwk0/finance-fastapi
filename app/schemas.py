from decimal import Decimal
from pydantic import BaseModel, Field, field_validator

class OperationRequest(BaseModel):
    wallet_name: str = Field(..., max_length=150)
    amount: Decimal
    description: str | None = Field(None, max_length=250)

    @field_validator("amount")
    def check_amount(cls, v: float) -> float:
        if v <= 0:
            raise ValueError("Amount must be positive")
        return v

    @field_validator("wallet_name")
    def check_wn(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Wallet name is empty")
        return v


class CreateWalletRequest(BaseModel):
    name: str = Field(..., max_length=50)
    initial_balance: Decimal = 0

    @field_validator("name")
    def check_name(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Wallet name is empty")
        return v

    @field_validator("initial_balance")
    def check_ib(cls, v: Decimal) -> Decimal:
        if v < 0:
            raise ValueError("Amount cant be negative")
        return v