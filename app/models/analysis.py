from pydantic import BaseModel


class Analysis(BaseModel):
    analysis_id: int
    status: str
