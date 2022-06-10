from pydantic import BaseModel
from typing import Optional


class SendEmail(BaseModel):
    sender: str
    recipient: str
    subject: Optional[str] = None
    body: str

    login: str
    password: str


class GetEmail(BaseModel):
    filter_from: Optional[str] = None
    filter_to: Optional[str] = None

    login: str
    password: str


class Proxy(BaseModel):
    ip: Optional[str] = None
