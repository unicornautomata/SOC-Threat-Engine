from typing import Optional
from pydantic import BaseModel


class Alert(BaseModel):
    severity: str
    message: str
    indicator: Optional[str] = None
