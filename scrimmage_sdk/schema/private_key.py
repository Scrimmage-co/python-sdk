from pydantic import BaseModel


class PrivateKey(BaseModel):
    alias: str
    value: str
