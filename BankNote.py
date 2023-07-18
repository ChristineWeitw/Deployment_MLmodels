# pydantic enforces type hints at runtime, and provides user friendly errors when data is invalid.
# Define how data should be in pure, canonnical python; validate it with pydantic

from pydantic import BaseModel
class BankNote(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float