from typing import Optional
from pydantic import BaseModel


class Host(BaseModel):
    ip: str
    hostname: Optional[str] = None
    risk_score: int = 0
