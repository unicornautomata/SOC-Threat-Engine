from pydantic import BaseModel

class Event(BaseModel):

    timestamp: str
    src_ip: str
    dst_ip: str
    protocol: str
    value: str